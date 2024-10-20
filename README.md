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
```

Clone the repository:

```bash
git clone https://github.com/greg1703/XploitHunter.git
```

Navigate into the project directory:

```bash
cd XploitHunter
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the scanner, run the following command:

```bash
python XploitHunter.py
```

When prompted, enter the target URL that you want to scan (make sure you have authorization).

Example:

```bash
Enter the target URL: http://example.com
```

## Vulnerabilities Detected

- **SQL Injection**: Attempts to inject SQL payloads into URL parameters and checks for database errors.
- **XSS**: Injects JavaScript payloads into HTML forms and checks if they are reflected.
- **CSRF**: Checks if the forms on the website contain CSRF tokens.
- **Insecure Headers**: Scans for missing security headers.
- **Directory Traversal**: Attempts to access restricted directories using path traversal payloads.
- **File Uploads**: Scans for file upload forms and attempts to upload a test file.

## Example Output

```
Enter the target URL: http://example.com

[+] Scanning for SQL Injection vulnerabilities...
[!] Potential SQL Injection vulnerability found with payload: ' OR '1'='1

[+] Scanning for XSS vulnerabilities...
[!] Potential XSS vulnerability found in form action: http://example.com/login

[+] Checking for CSRF protection...
[!] CSRF token missing in form action: http://example.com/login

[+] Scanning HTTP headers for security...
[!] Missing security headers: Strict-Transport-Security, Content-Security-Policy

[+] Scanning for directory traversal vulnerabilities...
[!] Potential directory traversal vulnerability found with payload: ../../etc/passwd

[+] Checking for insecure file uploads...
[!] Insecure file upload detected at: http://example.com/upload
```

## Contribution

Feel free to contribute by opening issues or submitting pull requests to improve the tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
