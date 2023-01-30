import os
import json
import argparse
import requests

banner = """
    ______            __  __  _____  __ 
   / __/ /  ___  ____/ /_/ / / / _ \/ / 
  _\ \/ _ \/ _ \/ __/ __/ /_/ / , _/ /__
 /___/_//_/\___/_/  \__/\____/_/|_/____/
"""

def read_urls_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: file not found: {filename}")
        return []

os.system("clear")
print(banner)
parser = argparse.ArgumentParser(description='Shorten a URL')
parser.add_argument('-m', '--mode', type=str, choices=['single', 'mass'], help='The mode of operation (single or mass)')
parser.add_argument('-u', '--url', type=str, help='The URL to shorten (single mode only)')
parser.add_argument('-f', '--file', type=str, help='A file containing the URLs to shorten (mass mode only)')
args = parser.parse_args()

mode = args.mode
if mode == 'single':
    if not args.url:
        parser.print_usage()
        exit()
    urls_to_shorten = [args.url]
elif mode == 'mass':
    if not args.file:
        parser.print_usage()
        exit()
    urls_to_shorten = read_urls_from_file(args.file)
else:
    parser.print_usage()
    exit()

url = "https://url-shortener-service.p.rapidapi.com/shorten"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "3398693b48msh311dd6a4dbdd27bp19903ajsn7fcf6c888dda",
	"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
}

for url_to_shorten in urls_to_shorten:
    payload = f"url={url_to_shorten}"
    response = requests.request("POST", url, data=payload, headers=headers)

    response_json = json.loads(response.text)
    result_url = response_json.get('result_url')

    if result_url:
        print(f"Shortened URL: {result_url}")
    else:
        print(f"Unable to shorten URL: {url_to_shorten}")
