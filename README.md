# 🔐 Jagspire Security Log Analyzer

A beginner-friendly Python-based security log analysis tool developed as part of the **Jagspire Cyber Security Internship – Week 1**.

The project analyzes system/security logs, identifies suspicious login activity, counts failed authentication attempts by IP address, and detects potential brute-force sources.

---

## 📌 Project Overview

Security logs contain valuable information about user activity, authentication attempts, and potential security incidents.

Manually analyzing large numbers of logs can be time-consuming. This project demonstrates how Python can be used to automate basic security log analysis.

The analyzer reads a log file, identifies failed login attempts, extracts IP addresses, counts repeated failures, and generates a security report.

---

## 🎯 Objectives

The main objectives of this project are:

* Learn basic security log analysis
* Practice Python file handling
* Work with regular expressions
* Extract IP addresses from logs
* Identify failed authentication attempts
* Detect potential brute-force activity
* Generate an automated security report
* Practice Git and GitHub workflow

---

## 🛠️ Technologies Used

* **Python 3**
* **Regular Expressions (`re`)**
* **File Handling**
* **Collections / Counter**
* **Git**
* **GitHub**
* **VS Code**

No external Python packages are required.

---

## 📂 Project Structure

```text
jagspire-security-log-analyzer/
│
├── log_parser.py
├── sample_logs.txt
├── suspicious_logs.txt
├── security_report.txt
├── README.md
└── requirements.txt
```

### File Description

| File                  | Description                        |
| --------------------- | ---------------------------------- |
| `log_parser.py`       | Main Python security log analyzer  |
| `sample_logs.txt`     | Sample security log input          |
| `suspicious_logs.txt` | Filtered suspicious events         |
| `security_report.txt` | Generated security analysis report |
| `README.md`           | Project documentation              |
| `requirements.txt`    | Project dependency information     |

---

## ⚙️ Features

### 1. Log File Reading

The program reads security events from a text file.

### 2. Suspicious Event Detection

The analyzer searches for events containing keywords such as:

* Failed login
* Authentication failed
* Invalid login
* Unauthorized

### 3. IP Address Extraction

The program uses Python regular expressions to extract IPv4 addresses from log entries.

### 4. Failed Login Analysis

Failed login attempts are counted for each detected IP address.

### 5. Brute-Force Detection

If an IP address generates **3 or more failed login attempts**, it is flagged as a potential brute-force source.

> The threshold is intended for this educational project and should not be treated as a production detection rule.

### 6. Automated Report Generation

The program generates:

```text
suspicious_logs.txt
security_report.txt
```

---

## 🚀 Installation

### Step 1 — Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2 — Enter the project directory

```bash
cd jagspire-security-log-analyzer
```

### Step 3 — Check Python installation

```bash
python --version
```

Python 3.x is recommended.

---

## ▶️ Running the Project

Run:

```bash
python log_parser.py
```

The program analyzes `sample_logs.txt` and generates the output files automatically.

---

## 📊 Example Input

Example entries from `sample_logs.txt`:

```text
2026-08-07 09:15:22 INFO User admin logged in successfully from 192.168.1.10
2026-08-07 09:16:03 WARNING Failed login attempt for user admin from 192.168.1.20
2026-08-07 09:16:15 WARNING Failed login attempt for user admin from 192.168.1.20
2026-08-07 09:16:28 WARNING Failed login attempt for user admin from 192.168.1.20
```

The analyzer identifies the repeated failed login attempts from:

```text
192.168.1.20
```

---

## 📈 Example Output

```text
==================================================
      JAGSPIRE SECURITY LOG ANALYZER
==================================================

Total log entries: 10
Suspicious entries: 6

Failed login attempts:
  192.168.1.20: 3
  10.0.0.25: 3

Potential brute-force sources:
  [ALERT] 192.168.1.20 -> 3 failed attempts
  [ALERT] 10.0.0.25 -> 3 failed attempts

Files generated:
  suspicious_logs.txt
  security_report.txt

Analysis completed successfully.
```

---

## 🔎 Security Concepts Demonstrated

This project provides practical exposure to:

* Security log analysis
* Authentication monitoring
* Suspicious activity detection
* Brute-force attack detection
* IP address analysis
* Basic security automation
* Security alert generation

---

## 🧠 What I Learned

Through this project, I practiced:

* Python functions
* File handling
* String processing
* Regular expressions
* Dictionaries and counters
* Exception handling
* Basic security analysis
* Git version control
* GitHub repository management

---

## 🔮 Future Improvements

Possible improvements include:

* Real-time log monitoring
* Support for Apache/Nginx logs
* Windows Event Log support
* Linux authentication log support
* IP reputation checking
* Threat Intelligence API integration
* MITRE ATT&CK technique mapping
* Web-based dashboard
* Email/Slack security alerts
* Machine-learning-based anomaly detection
* AI-powered security investigation

---

## ⚠️ Disclaimer

This project is created for **educational and internship purposes**.

The detection rules are intentionally simple and should not be considered a complete production-grade security monitoring system.

---

## 👨‍💻 Internship

**Program:** Jagspire Cyber Security Internship
**Week:** Week 1
**Project:** Security Log Analyzer
**Language:** Python

---

## 📜 License

This project is intended for educational use.
