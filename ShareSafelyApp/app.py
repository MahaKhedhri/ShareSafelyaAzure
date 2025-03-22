from flask import Flask, request, redirect, url_for, render_template
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from datetime import datetime, timedelta

app = Flask(__name__)

# Configuration
KEY_VAULT_NAME = 'myKeyVaultShareSafely'  
STORAGE_ACCOUNT_NAME = 'sharesafelystrg'
CONTAINER_NAME = 'uploads'
SECRET_NAME = 'blob-storage-account-key'  # The name of the secret in Key Vault

# Construct the Key Vault URL
key_vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net"

# Use DefaultAzureCredential to authenticate
credential = DefaultAzureCredential()

# Initialize the SecretClient to interact with the Key Vault
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# Fetch the ACCOUNT_KEY from Key Vault
secret = secret_client.get_secret(SECRET_NAME)
ACCOUNT_KEY = secret.value

# Construct the connection string for Azure Blob Storage
connection_string = (
    f"DefaultEndpointsProtocol=https;"
    f"AccountName={STORAGE_ACCOUNT_NAME};"
    f"AccountKey={ACCOUNT_KEY};"
    f"EndpointSuffix=core.windows.net"
)

# Initialize BlobServiceClient with the connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:  # Ensure the file is valid and has a filename
            blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.filename)
            blob_client.upload_blob(file, overwrite=True)
            sas_token = generate_blob_sas(
                account_name=STORAGE_ACCOUNT_NAME,
                container_name=CONTAINER_NAME,
                blob_name=file.filename,
                account_key=ACCOUNT_KEY,  # Provide the account key here
                permission=BlobSasPermissions(read=True),
                expiry=datetime.utcnow() + timedelta(seconds=15)
            )
            sas_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{file.filename}?{sas_token}"
            return redirect(url_for('file_link', url=sas_url))
    return render_template('upload.html')

@app.route('/link')
def file_link():
    url = request.args.get('url')
    return render_template('link.html', url=url)

if __name__ == '__main__':
    app.run(debug=True)