import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

# Function to check if the URL is valid
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Ask user for inputs
url = input("Enter the website URL: ")

# Validate the URL
if not is_valid_url(url):
    print("❌ Invalid URL. Please check the URL and try again.")
else:
    tag = input("Enter the HTML tag to extract (e.g., 'p', 'h1', 'a'): ")

    try:
        # Try to access the page
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # If extracting links, look for 'a' tags with 'href'
        if tag == 'a':
            elements = soup.find_all('a', href=True)
            data = []
            for i, element in enumerate(elements, start=1):
                link = element['href']
                print(f"{i}. {link}")
                data.append({'Index': i, 'Link': link})

            # Save to CSV
            if data:
                df = pd.DataFrame(data)
                df.to_csv('links_output.csv', index=False)
                print("\n✅ Links saved to links_output.csv")
            else:
                print("\n❌ No links found.")
        else:
            # For other tags
            elements = soup.find_all(tag)
            data = []
            for i, element in enumerate(elements, start=1):
                text = element.get_text(strip=True)
                print(f"{i}. {text}")
                data.append({'Index': i, 'Content': text})

            # Save to CSV for other tags
            if data:
                df = pd.DataFrame(data)
                df.to_csv('output.csv', index=False)
                print("\n✅ Data saved to output.csv")
            else:
                print("\n❌ No elements found.")

    except requests.exceptions.RequestException as e:
        if "No connection adapters" in str(e):
            print("❌ Invalid URL. Please check the URL and try again.")
        else:
            print(f"❌ Error with the request: {e}")
