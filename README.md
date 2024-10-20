# XploitHunter
XploitHunter is a Python-based tool designed to scan websites for common vulnerabilities, including SQL Injection, XSS, CSRF, insecure headers, directory traversal and insecure file uploads.This tool helps developers ensure their websites adhere to basic security standards by identifying potential flaws in their web applications.

Disclaimer: This tool is intended for educational purposes only. You should only scan websites that you have explicit permission to test. Unauthorized scanning of websites is illegal and may violate cybersecurity laws.

## Features

- **SQL Injection Detection**: Scans for potential SQL injection vulnerabilities by sending SQL payloads.
- **Cross-Site Scripting (XSS) Detection**: Identifies XSS vulnerabilities by injecting JavaScript payloads in forms.
- **Cross-Site Request Forgery (CSRF)**: Detects the presence or absence of CSRF tokens in forms.
- **Insecure HTTP Headers**: Analyzes the security of HTTP headers like `Content-Security-Policy`, `X-Frame-Options`, `Strict-Transport-Security`.
- **Directory Traversal Detection**: Attempts directory traversal attacks to access restricted files.
- **Insecure File Uploads**: Detects websites that allow potentially dangerous files to be uploaded and executed.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the dependencies using:

```bash
pip install -r requirements.txt

## Installation
1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/XploitHunter.git

2. Navigate into the project directory:
cd XploitHunter

3. Install the required dependencies:
pip install -r requirements.txt
