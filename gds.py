import subprocess
import re

def extract_id(url):
    # Extract file ID from URL
    file_id = re.search(r'(?<=/d/).+?(?=/|$)', url)
    return file_id.group() if file_id else None

def get_streaming_url(file_id, api_key):
    # Construct the streaming URL
    streaming_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?key={api_key}&alt=media"

    return streaming_url

def main():
    shared_link = input("Please enter the Google Drive shared link: ")
    # api_key = input("Please enter your Google API key: ")
    api_key = ""
    file_id = extract_id(shared_link)
    if not file_id:
        print("Invalid Google Drive shared link.")
        return

    streaming_url = get_streaming_url(file_id, api_key)

    # Open the streaming URL with VLC
    subprocess.call(['vlc', streaming_url])

if __name__ == '__main__':
    main()
