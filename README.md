# 🔐 Secure Cloud Storage

A secure cloud storage system built from scratch in Python to explore real-world cybersecurity concepts, secure software development, and backend engineering.

> This project is being developed incrementally with a focus on learning industry-standard security practices rather than just building features.

---

## 📊 Project Status

- ✅ Phase 1 Completed
- 🚧 Phase 2 In Progress
- 🔜 Phase 3 Planned
- 🔜 Phase 4 Planned

## ✨ Current Features

### Authentication
- User Registration & Login
- Password hashing using **bcrypt**
- SQLite-based user management
- Duplicate username prevention

### File Management
- Upload files
- Download files
- Delete files
- Restore deleted files (Recycle Bin)
- Permanent file deletion
- Search files
- Dashboard with storage statistics

### Security
- File encryption using Fernet (AES-based symmetric encryption)
- Secure password hashing with bcrypt
- Activity logging
- User isolation for stored files

### Database
- SQLite integration
- Automatic database initialization
- Users stored in relational database instead of JSON

---

## 🛠 Tech Stack

- Python 3
- SQLite
- bcrypt
- Cryptography (Fernet)
- Git & GitHub

---

## 📂 Project Structure

```
SecureCloudStorage/
│
├── app.py
├── database/
│   └── secure_cloud.db
├── keys/
├── logs/
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
└── requirements.txt
```

---

## 🚀 Project Roadmap

### ✅ Phase 1 (Completed)
- CLI application
- Authentication
- File encryption
- Upload / Download
- Recycle Bin
- Activity Logs

### 🚧 Phase 2 (In Progress)
- SQLite migration ✅
- bcrypt authentication ✅
- File metadata management
- SHA-256 integrity verification
- Storage quotas
- Per-user encryption keys

### 🔜 Phase 3
- Flask Web Interface
- User Dashboard
- REST APIs

### ☁️ Phase 4
- AWS Deployment
- Object Storage
- Docker
- HTTPS

---

## 📈 What I'm Learning

This project is helping me gain practical experience with:

- Secure Authentication
- Cryptography
- Password Security
- SQLite & Databases
- File Systems
- Backend Development
- Software Architecture
- Git & GitHub
- Secure Coding Practices

---

## 📌 Upcoming Features

- SHA-256 file integrity verification
- Metadata management
- Storage quotas
- Per-user encryption keys
- Cloud deployment
- JWT Authentication
- HTTPS
- Docker

---

## ⭐ Author

**Rutul Parate**

Cybersecurity Student | Python | Backend Development | Secure Software Engineering

This repository documents my journey of building a secure cloud storage system while learning real-world software engineering and cybersecurity concepts.