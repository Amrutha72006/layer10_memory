import requests
import json
import os

REPO = "microsoft/vscode"

url = f"https://api.github.com/repos/{REPO}/issues/comments"

params = {
    "per_page": 50
}

response = requests.get(url, params=params)

comments = response.json()

os.makedirs("data", exist_ok=True)

with open("data/comments.json", "w", encoding="utf-8") as f:
    json.dump(comments, f, indent=2)

print("Downloaded comments:", len(comments))