# 🔐 ShareSafely – Secure File Sharing Web App (AZURE)

**ShareSafely** is a secure file-sharing web application built with Python and Flask, designed to offer short-lived, secure access to uploaded files. Users can upload files, which are then stored in **Azure Blob Storage**. For every upload, the app generates a unique, **time-limited download link (15 seconds)**. After the time expires, the link becomes invalid — ensuring strong protection for sensitive files.


## 🚀 Features

- 🔒 **Secure Uploads**: Files are stored in Azure Blob Storage with secure access policies.
- ⏱️ **Expiring Links**: Each file generates a unique link that expires after 15 seconds.
- 🧼 **Automatic Cleanup**: Expired files or links can be cleaned using Azure Functions.
- 👁️ **Monitoring**: Application health and performance are tracked using Azure Monitor.
- 🔐 **Secret Management**: All sensitive keys and secrets are stored securely in Azure Key Vault.
  

## 🛠️ Technologies Used

| Technology          | Purpose                              |
|---------------------|--------------------------------------|
| **Python (Flask)**  | Backend web framework                |
| **Azure Blob Storage** | Secure file storage                 |
| **Azure Web Apps**  | Hosting the Flask app                |
| **Azure Key Vault** | Secure management of secrets         |
| **Azure Monitor**   | Logging, metrics, and alerting       |
| **Azure Functions** | Automation (e.g., cleanup tasks)     |


## 📁 How It Works

1. A user uploads a file through the web interface.
2. The file is saved securely in Azure Blob Storage.
3. A **unique, time-sensitive download link** is generated (valid for 15 seconds).
4. After 15 seconds, the link becomes invalid, preventing unauthorized access.
5. Optionally, old files can be cleaned up with an automated Azure Function.


## 🔐 Security Considerations
All file access is token-based and temporary.
Secrets and keys are never stored in code — they are retrieved from Azure Key Vault.
HTTPS enforced via Azure Web Apps.
Expired tokens prevent link reuse or file leaks.


## 🚀 How to Use

1. Clone the repo:
   ```bash
      https://github.com/MahaKhedhri/ShareSafelyaAzure.git


## 📖 Documentation and Setup Instructions

For detailed setup, deployment, and usage steps, please refer to the [`Presentation.docs`](./Presentation.docs) file included in this repository.


## 📸 Screenshots
![Web App](https://imgur.com/0usJFQh.jpg)
![Storage Acc](https://imgur.com/C8Vp8eW.jpg)


## ✍️ Author
Maha Khedhri 
Big Data and Web Development Student
