import requests
import os

def secure_request(url):
    # FIX: Ensure we only visit trusted sites and enable SSL verification
    if not url.startswith("https://"):
        print("Insecure URL blocked.")
        return None
    
    # verify=True is the default, but we'll be explicit for the assignment
    response = requests.get(url, verify=True)
    return response

def main():
    # FIX: Remove hardcoded password. Fetch from environment instead.
    db_password = os.getenv("DB_PASSWORD") 
    print("Connecting to database securely...")
    
    secure_request("https://example.com")

if __name__ == "__main__":
    main()
