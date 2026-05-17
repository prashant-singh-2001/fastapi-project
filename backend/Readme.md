# FastAPI Project

A simple backend project built using FastAPI.

---

# Clone Repository

```bash
git clone https://github.com/prashant-singh-2001/fastapi-project.git
```

---

# Project Setup

## 1. Navigate to Project Folder

```bash
cd fastapi-project
```

---

## 2. Run Setup Script

### Windows

```bash
setup.windows.bat
```

### Linux / Mac

```bash
./setup.linux.sh
```

This script will:

* Create a virtual environment
* Install dependencies from `requirements.txt`
* Prepare the project for execution

---

# Run the Application

Open terminal inside the project folder and run:

```bash
uvicorn server:app --reload
```

---

# API Access

Once the server starts, open:

## Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

## ReDoc Documentation

```text
http://127.0.0.1:8000/redoc
```

---

# Project Structure

```text
fastapi-project/
│
├── venv/
├── requirements.txt
├── setup.bat
├── setup.sh
├── server.py
└── README.md
```

---

# Requirements

* Python 3.10+
* FastAPI
* Uvicorn

---

# Install Dependencies Manually

If setup scripts are not used:

```bash
pip install -r requirements.txt
```

---

# Development Server

Run with auto reload:

```bash
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

---

# Author

Prashant Singh

GitHub:
[prashant-singh-2001 GitHub](https://github.com/prashant-singh-2001?utm_source=chatgpt.com)
