import requests

def download_links_file(server_url):
    url = f"{server_url}/get_links"
    response = requests.get(url)

    if response.status_code == 200:
        with open('downloaded_links.txt', 'wb') as f:
            f.write(response.content)
        print("File downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

if __name__ == "__main__":
    server_url = 'https://ecb17473-fec1-4c63-9f25-b864aa977b93-00-9e9l9f3np543.picard.replit.dev/'  # Replace <server-ip> with the actual IP address of your Flask server
    download_links_file(server_url)
