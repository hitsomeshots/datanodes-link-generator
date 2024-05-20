import os
import requests

from urllib.parse import urlparse

def get_download_link(download_url):
    parsed_url = urlparse(download_url)
    path_segments = parsed_url.path.split('/')

    file_code = path_segments[1]
    file_name = path_segments[-1]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'lang=english; file_name={file_name}; file_code={file_code};',
        'Host': 'datanodes.to',
        'Origin': 'https://datanodes.to',
        'Referer': 'https://datanodes.to/download',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    payload = {
        'op': 'download2',
        'id': file_code,
        'rand': '',
        'referer': 'https://datanodes.to/download',
        'method_free': 'Free Download >>',
        'method_premium': ''
    }

    response = requests.post("https://datanodes.to/download", data=payload, headers=headers, allow_redirects=False)

    if response.status_code == 302:
        redirect_url = response.headers.get('Location')
        return redirect_url
    else:
        return None

if __name__ == "__main__":
    if not os.path.exists('links.txt'):
        with open('links.txt', 'w') as file:
            exit()
            
    with open('links.txt', 'r') as file:
        urls = file.readlines()

    with open('output_links.txt', 'a') as output_file:
        for url in urls:
            url = url.strip()
            if url:
                output_file.write(get_download_link(url) + '\n')

    print("[*] Done generating download links!")