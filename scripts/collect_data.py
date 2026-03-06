import requests
import json
import os

# choose a public repo
REPO = "microsoft/vscode"

url = f"https://api.github.com/repos/{REPO}/issues"

params = {
    "state": "all",
    "per_page": 30
}

response = requests.get(url, params=params)

issues = response.json()

os.makedirs("data", exist_ok=True)

with open("data/issues.json", "w", encoding="utf-8") as f:
    json.dump(issues, f, indent=2)

print(f"Downloaded {len(issues)} issues")