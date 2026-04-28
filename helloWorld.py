import requests

def insecure_request(url):
    # This function makes an insecure HTTP request without proper error handling
    response = requests.get(url, verify=False)
    return response

def main():
    # Hardcoded password - sensitive information exposed
    password = "admin123"
    print("Connecting to database...")
    insecure_request("http://example.com")

if __name__ == "__main__":
    main()
