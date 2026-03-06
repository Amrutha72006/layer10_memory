import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("data/issues.json", "r", encoding="utf-8") as f:
    issues = json.load(f)

entities = []

for issue in issues:

    title = issue.get("title") or ""
    body = issue.get("body") or ""

    text = title + " " + body

    doc = nlp(text)

    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "type": ent.label_
        })

with open("data/entities.json", "w") as f:
    json.dump(entities, f, indent=2)

print("Entities extracted:", len(entities))