import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

INPUT_FILE = "data/issues.json"
OUTPUT_FILE = "data/extracted_claims.json"


def build_prompt(issue):
    text = f"""
You are an information extraction system.

Extract structured knowledge from this GitHub issue.

Return JSON ONLY.

Schema:
{{
  "entities": [
    {{"type": "Person|Issue|Label", "name": ""}}
  ],
  "claims": [
    {{
      "relation": "OPENED|COMMENTED_ON|CLOSED|ASSIGNED_TO|LABELED_AS|MENTIONED",
      "source": "",
      "target": "",
      "evidence_excerpt": "",
      "timestamp": ""
    }}
  ]
}}

Issue Title:
{issue.get("title")}

Issue Body:
{issue.get("body")}
"""
    return text


def extract(issue):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": build_prompt(issue)}],
        temperature=0,
    )

    return response.choices[0].message.content


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        issues = json.load(f)

    results = []

    for issue in tqdm(issues[:30]):   # limit for speed + cost
        try:
            output = extract(issue)
            results.append(output)
        except Exception as e:
            print("Error:", e)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("Extraction complete.")


if __name__ == "__main__":
    main()