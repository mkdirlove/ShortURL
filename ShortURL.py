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

os.system("clear")
print(banner)
parser = argparse.ArgumentParser(description='Shorten a URL')
parser.add_argument('-u', '--url', type=str, required=True, help='The URL to shorten')
args = parser.parse_args()

if not args.url:
    parser.print_usage()
    exit()
    
url = "https://url-shortener-service.p.rapidapi.com/shorten"
payload = f"url={args.url}"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "3398693b48msh311dd6a4dbdd27bp19903ajsn7fcf6c888dda",
	"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

response_json = json.loads(response.text)
result_url = response_json.get('result_url')

if result_url:
    print(f" Shorten URL: {result_url}\n")
else:
    print(f" Unable to shorten URL: {args.url}\n")
