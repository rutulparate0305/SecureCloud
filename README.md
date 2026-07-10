# 🔐 Secure Cloud Storage

A secure cloud storage system built from scratch in Python to explore real-world cybersecurity concepts, secure software development, encryption, and backend engineering.

> This project is being developed incrementally with a focus on implementing industry-standard security practices rather than simply building features.

---

# 📊 Project Status

- ✅ Phase 1 Completed
- ✅ Phase 2 Completed
- 🔜 Phase 3 Planned (Flask Web Application)
- 🔜 Phase 4 Planned (Cloud Deployment)

---

# ✨ Features

## 🔑 Authentication

- User Registration & Login
- Secure password hashing using **bcrypt**
- SQLite-based user management
- Duplicate username prevention

## 📁 File Management

- Secure file upload
- Secure file download
- Delete files
- Restore deleted files (Recycle Bin)
- Permanent file deletion
- File search
- User dashboard with storage statistics

## 🔒 Security

- File encryption using **Fernet** (AES-based symmetric encryption)
- **Unique encryption key generated for every registered user**
- Secure password hashing with **bcrypt**
- SHA-256 checksum generation for file integrity verification
- User activity logging
- User-isolated encrypted storage

## 🗄 Database

- SQLite relational database
- Automatic database initialization
- User authentication data
- File metadata management
- Per-user encryption key management

---

# 🏗 Architecture

```
                User
                  │
                  ▼
        Authentication (bcrypt)
                  │
                  ▼
            SQLite Database
        ┌─────────┼─────────┐
        │         │         │
      Users    File Metadata  Encryption Keys
                  │
                  ▼
         Encryption Layer (Fernet)
                  │
                  ▼
          Encrypted File Storage
```

---

# 🛠 Tech Stack

- Python 3
- SQLite
- bcrypt
- Cryptography (Fernet)
- hashlib (SHA-256)
- Git
- GitHub

---

# 📂 Project Structure

```
SecureCloudStorage/
│
├── app.py
├── database/
│   └── secure_cloud.db
├── logs/
│   └── activity.log
├── storage/
│   ├── encrypted/
│   ├── downloads/
│   ├── recycle_bin/
│   └── uploads/
├── utils/
│   ├── auth.py
│   ├── database.py
│   ├── encryption.py
│   ├── file_handler.py
│   ├── logger.py
│   └── password.py
├── requirements.txt
└── README.md
```

---

# 🚀 Project Roadmap

## ✅ Phase 1 – Core CLI Application

- User Authentication
- File Upload & Download
- Encryption
- Recycle Bin
- Activity Logs

## ✅ Phase 2 – Secure Backend

- SQLite Migration
- bcrypt Password Authentication
- File Metadata Management
- SHA-256 File Integrity
- Per-user Encryption Keys
- Metadata Synchronization
- Storage Statistics Dashboard

## 🔜 Phase 3 – Flask Web Application

- User Authentication Portal
- Interactive Dashboard
- REST APIs
- Responsive User Interface

## ☁️ Phase 4 – Cloud Deployment

- AWS Deployment
- Amazon S3 Storage
- Docker Containerization
- HTTPS
- Secure Environment Variables

---

# 🔒 Security Highlights

- Passwords are never stored in plaintext.
- Every registered user receives a unique encryption key.
- Files remain encrypted while stored.
- SHA-256 checksums provide integrity verification.
- User activities are logged for auditing.
- File metadata is managed securely using SQLite.

---

# 📚 What I'm Learning

This project is helping me gain practical experience with:

- Secure Authentication
- Cryptography
- Encryption & Key Management
- Password Security
- SQLite Databases
- Backend Development
- File Systems
- Software Architecture
- Secure Coding Practices
- Git & GitHub Workflow

---

# 🚀 Future Improvements

- Flask Web Interface
- User Profile Dashboard
- Role-Based Access Control (RBAC)
- JWT Authentication
- Multi-Factor Authentication (MFA)
- Secure File Sharing
- Storage Quotas
- AWS S3 Integration
- Docker Deployment
- HTTPS Support

---

# ⭐ Author

**Rutul Parate**

Cybersecurity & Cloud Computing Enthusiast

This repository documents my journey of building a secure cloud storage system while learning real-world cybersecurity principles, backend engineering, cryptography, and secure software development.