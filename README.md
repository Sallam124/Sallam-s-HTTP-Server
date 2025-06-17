# Sallam-s-HTTP-Server

## 🚀 Overview

This project implements a fully functional web server to understand how HTTP, concurrency, and low-level networking work under the hood. Inspired by the philosophy of "Build Your Own X," the server is written from scratch to explore:

- HTTP 1.1 protocol implementation  
- Multi-threaded request handling  
- Basic routing and static content serving  
- Logging and error responses  
- TLS (HTTPS) support *(in progress)*

---

## 🧠 Key Concepts

- 📡 Low-level socket programming (TCP/IP)  
- ⚙️ Multi-threading and concurrency control  
- 📜 HTTP request parsing and response formatting  
- 🔐 (Optional) TLS/SSL encryption via OpenSSL  
- 🗂️ Routing, file serving, and MIME type detection  

---

## 🛠️ Features

- HTTP 1.1 request handling  
- Static file serving (HTML, CSS, JS)  
- Basic routing (e.g., `/`, `/about`, `/contact`)  
- Multi-threaded client handling  
- Logging of incoming requests  
- Error handling (404, 500, malformed requests)  
- HTTPS/TLS support (optional via OpenSSL)  
- RESTful endpoint support (`GET`, `POST`, etc.)  

---

## 📁 Project Structure

```

/sallams-http-server/
│
├── server.py (or server.cpp)
├── router.py (or routing.cpp/.h)
├── logger.py
├── static/           # Folder to serve static files
│   └── index.html
├── certs/            # SSL certificate files (optional)
│   └── cert.pem
│   └── key.pem
└── README.md

```

### 🔧 Requirements

- Python 3.10+ / C++17+ (depending on implementation)  
- OpenSSL (for TLS support)  
- `make` or equivalent build system (for C++)  

