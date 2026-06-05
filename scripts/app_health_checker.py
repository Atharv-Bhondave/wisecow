import urllib.request
import urllib.error
import sys

def check_application_health(url):
    print(f"Checking health of the application at: {url}")
    try:
        # Send an HTTP request with a 5-second timeout
        response = urllib.request.urlopen(url, timeout=5)
        status_code = response.getcode()
        
        # HTTP status codes 200-299 are considered successful ("UP")
        if 200 <= status_code < 300:
            print(f"Application Status: UP (HTTP {status_code}) - The application is functioning correctly.")
            return True
        else:
            print(f"Application Status: DOWN (HTTP {status_code}) - Unexpected status code returned.")
            return False
            
    except urllib.error.HTTPError as e:
        # Server returned an error status code (e.g., 404, 500)
        print(f"Application Status: DOWN (HTTP {e.code}) - Server returned an error: {e.reason}")
        return False
    except urllib.error.URLError as e:
        # Server could not be reached (e.g., DNS error, connection refused)
        print(f"Application Status: DOWN - The application is unreachable. Reason: {e.reason}")
        return False
    except Exception as e:
        # Handle other exceptions like timeout
        print(f"Application Status: DOWN - Application check failed. Error: {str(e)}")
        return False

if __name__ == "__main__":
    # Check if custom URL is provided as a command-line argument, fallback to local Wisecow port 4499
    target_url = "http://localhost:4499"
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        
    check_application_health(target_url)
