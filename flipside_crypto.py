api_key = "50709c53-5892-4664-aee0-bbbd4ad7bae0"

import requests

url = f"https://api.flipsidecrypto.com/api/v2/metrics/projects?api_key={api_key}"

metrics_url = f"https://api.flipsidecrypto.com/api/v2/projects/metrics?api_key={api_key}"

payload={}
headers = {}

response = requests.request("GET", metrics_url, headers=headers, data=payload)

print(response.json())
