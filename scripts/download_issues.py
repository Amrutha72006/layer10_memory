import requests
import json
import time

OWNER = "pallets"
REPO = "flask"

PER_PAGE = 50
MAX_PAGES = 2

all_issues = []

for page in range(1, MAX_PAGES + 1):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    params = {
        "state": "all",
        "per_page": PER_PAGE,
        "page": page
    }

    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        break

    data = response.json()
    all_issues.extend(data)

    print(f"Downloaded page {page}")
    time.sleep(1)

with open("data/issues.json", "w", encoding="utf-8") as f:
    json.dump(all_issues, f, indent=2)

print("Saved", len(all_issues), "issues.")