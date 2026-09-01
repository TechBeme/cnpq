<div align="center">

# 🎓 CNPq Lattes Curriculum Downloader

**Automated tool to download CNPq Lattes curriculum vitae with reCAPTCHA bypass**

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green?logo=flask)](https://flask.palletsprojects.com/)
[![2Captcha](https://img.shields.io/badge/2Captcha-API-orange)](https://2captcha.com/)
[![License](https://img.shields.io/badge/License-Proprietary-red)](LICENSE)

[Features](#-key-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Configuration](#%EF%B8%8F-configuration) • [Usage](#-usage) • [License](#-license)

**Languages:** [🇧🇷 Português](README.md) • [🇪🇸 Español](README.es.md)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technology Stack](#%EF%B8%8F-technology-stack)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#%EF%B8%8F-configuration)
- [Usage](#-usage)
- [Service Deployment](#-service-deployment)
- [Project Structure](#-project-structure)
- [License](#-license)
- [Disclaimer](#%EF%B8%8F-disclaimer)

---

## 🎯 Overview

The **CNPq Lattes Curriculum Downloader** is an automated tool designed to download curriculum vitae from the CNPq Lattes Platform. The system automatically bypasses reCAPTCHA protection using the 2Captcha service, enabling seamless and efficient curriculum extraction.

**Key capabilities:**
- Automated reCAPTCHA solving with 2Captcha integration
- Flask web interface for easy curriculum downloads
- Cookie management for session handling
- Automatic XML curriculum extraction
- Local storage system for downloaded files
- Command-line script for batch processing
- Systemd service support for production deployment

**Perfect for:**
- Academic researchers
- HR departments
- Data collection projects
- Academic analysis
- Research institutions

---

## ✨ Key Features

### 🔐 reCAPTCHA Bypass
- Automatic reCAPTCHA solving using 2Captcha API
- High success rate with reliable token generation
- Error handling and retry mechanisms

### 🌐 Web Interface
- Clean and intuitive Flask-based web UI
- Real-time download status
- Form-based curriculum ID input
- Automatic file serving

### 💾 Storage Management
- Automatic local file storage in `resumes/` folder
- File caching to avoid duplicate downloads
- XML curriculum extraction from ZIP files
- Organized file naming with Lattes ID

### 🔄 Flexible Usage
- Web interface with Flask (`run.py`)
- Command-line script (`cnpq.py`)
- Alternative web UI (`render.py`)
- Systemd service for production deployment

### 📝 Logging
- Comprehensive logging system
- Debug information tracking
- Error reporting and monitoring

---

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|------------|---------|----------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.7+ | Core programming language |
| **Flask** | 3.0+ | Web framework for UI |
| **2Captcha** | Latest | reCAPTCHA solving service |
| **Requests** | Latest | HTTP client for web requests |
| **Gunicorn** | Latest | WSGI HTTP server for production |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- 2Captcha API key ([Get one here](https://2captcha.com/))
- CNPq Lattes ID (16-digit number)

### 1. Clone the Repository

```bash
git clone https://github.com/TechBeme/cnpq.git
cd cnpq
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure

Copy `config.ini.example` to `config.ini` and add your credentials:

```ini
[DEFAULT]
recaptcha_key = 6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI

[TWOCAPTCHA]
API_KEY = your_2captcha_api_key_here
```

### 4. Run the Web Interface

```bash
python run.py
```

Access the application at `http://localhost:5000`

---

## 📦 Installation

### Option 1: Standard Installation

```bash
# Clone repository
git clone https://github.com/TechBeme/cnpq.git
cd cnpq

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure
cp config.ini.example config.ini
# Edit config.ini with your credentials

# Run
python run.py
```

### Option 2: Production Deployment

```bash
# Install and configure as above
# Then set up systemd service

sudo cp cnpq.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable cnpq
sudo systemctl start cnpq
sudo systemctl status cnpq
```

---

## ⚙️ Configuration

### config.ini

Create a `config.ini` file based on `config.ini.example`:

```ini
[DEFAULT]
# CNPq reCAPTCHA site key (usually this one)
recaptcha_key = 6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI

[TWOCAPTCHA]
# Your 2Captcha API key
API_KEY = your_2captcha_api_key_here
```

### Getting Your 2Captcha API Key

1. Sign up at [2Captcha](https://2captcha.com/)
2. Navigate to your dashboard
3. Copy your API key
4. Paste it in the `config.ini` file

### Finding Lattes IDs

Lattes IDs are 16-digit numbers found in CNPq Lattes curriculum URLs:

```
http://lattes.cnpq.br/1234567890123456
                      ^^^^^^^^^^^^^^^^
                         Lattes ID
```

---

## 🎮 Usage

### Web Interface (Recommended)

1. Start the Flask server:
   ```bash
   python run.py
   ```

2. Open your browser and go to `http://localhost:5000`

3. Enter the Lattes ID (16 digits)

4. Click "Download"

5. The XML file will be automatically downloaded

**Note:** Downloaded files are stored in the `resumes/` folder with the format `{lattes_id}.xml`

### Command-Line Script

For single downloads without the web interface:

```bash
python cnpq.py
```

**Note:** Edit the script to set the desired Lattes ID before running.

### Alternative Web Interface

A simplified version without logging or caching:

```bash
python render.py
```

---

## 🚀 Service Deployment

### Systemd Service (Linux)

The included `cnpq.service` file allows you to run the application as a systemd service.

**Installation:**

```bash
# Copy service file
sudo cp cnpq.service /etc/systemd/system/

# Update paths in the service file if needed
sudo nano /etc/systemd/system/cnpq.service

# Reload systemd
sudo systemctl daemon-reload

# Enable service (start on boot)
sudo systemctl enable cnpq

# Start service
sudo systemctl start cnpq

# Check status
sudo systemctl status cnpq
```

**Management Commands:**

```bash
# Start
sudo systemctl start cnpq

# Stop
sudo systemctl stop cnpq

# Restart
sudo systemctl restart cnpq

# View logs
sudo journalctl -u cnpq -f
```

---

## 📁 Project Structure

```
cnpq/
├── cnpq.py               # Command-line script
├── run.py                # Main Flask application with logging
├── render.py             # Alternative Flask application
├── config.ini.example    # Configuration template
├── config.ini            # Your configuration (gitignored)
├── cnpq.service          # Systemd service file
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Web interface template
├── resumes/              # Downloaded curriculum files
└── cnpq.log              # Application logs
```

---

## 📝 License

**Proprietary License - All Rights Reserved**

Copyright © 2026 Rafael Vieira (TechBeme)

### ❌ Restrictions

- **No commercial use** without explicit permission
- **No modifications** or derivative works
- **No distribution** or sublicensing
- **No reverse engineering**
- **No public hosting** without authorization

### ✅ Permitted Use

- View source code for educational purposes
- Run for personal, non-commercial research use
- Fork for personal study only (not for distribution)

### 📧 Commercial Licensing

For commercial use, white-label solutions, or custom development:

**Contact:** [contact@techbe.me](mailto:contact@techbe.me)

---

## ⚠️ Disclaimer

This tool is provided for **educational and research purposes only**.

- This project is **independent** and **NOT affiliated** with CNPq or the Brazilian government
- Users are responsible for compliance with CNPq's Terms of Service
- Only collects publicly available data
- Built-in rate limiting to respect server resources
- Users must comply with applicable data protection laws (LGPD, GDPR, etc.)
- The developer is not responsible for misuse of this tool

**Use responsibly and ethically.**

---

## 🙏 Acknowledgments

Built with:
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [2Captcha](https://2captcha.com/) - reCAPTCHA solving service
- [Requests](https://requests.readthedocs.io/) - HTTP library
- [Gunicorn](https://gunicorn.org/) - WSGI HTTP server

---

<div align="center">

**Developed by [Rafael Vieira](https://github.com/TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

</div>