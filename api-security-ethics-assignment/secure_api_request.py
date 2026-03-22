
import os
import requests
def make_secure_api_request():
    # Retrieve the API key from an environment variable
    api_key = os.getenv('API_KEY')
    
    if not api_key:
        print("API key not found. Please set the API_KEY environment variable.")
        return
    
    # Define the endpoint
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Set up the headers with the API key
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        # Send a GET request to the endpoint
        response = requests.get(url, headers=headers)
        
        # Handle status codes
        if response.status_code == 200:
            print(response.json())
        elif response.status_code == 429:
            print("Rate limit reached. Try again later.")
        else:
            print(f"Request failed with status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    make_secure_api_request()

    

