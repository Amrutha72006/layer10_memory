import json
import re



with open("data/issues.json", "r", encoding="utf-8") as f:
    issues = json.load(f)

graph = {
    "nodes": [],
    "edges": []
}

REPO = "microsoft/vscode"

graph["nodes"].append({
    "id": REPO,
    "type": "Repository"
})

for issue in issues:

    issue_id = issue["id"]
    user = issue["user"]["login"]

    # Issue node
    graph["nodes"].append({
        "id": issue_id,
        "type": "Issue"
    })

    graph["edges"].append({
        "source": REPO,
        "target": issue_id,
        "relation": "HAS_ISSUE"
    })

    # Person node
    graph["nodes"].append({
        "id": user,
        "type": "Person"
    })

    # OPENED relationship
    graph["edges"].append({
        "source": user,
        "target": issue_id,
        "relation": "OPENED"
    })

    # ASSIGNED_TO relationship
    assignee = issue.get("assignee")
    if assignee:
        assignee_name = assignee["login"]

        graph["nodes"].append({
            "id": assignee_name,
            "type": "Person"
        })

        graph["edges"].append({
            "source": issue_id,
            "target": assignee_name,
            "relation": "ASSIGNED_TO"
        })

    # LABELED_AS relationship
    labels = issue.get("labels", [])

    for label in labels:
        label_name = label["name"]

        graph["nodes"].append({
            "id": label_name,
            "type": "Label"
        })

        graph["edges"].append({
            "source": issue_id,
            "target": label_name,
            "relation": "LABELED_AS"
        })

    # CLOSED relationship
    if issue.get("state") == "closed":

        closer = user

        graph["edges"].append({
            "source": closer,
            "target": issue_id,
            "relation": "CLOSED"
        })

    # MENTION detection
    title = issue.get("title") or ""
    body = issue.get("body") or ""
    text = title + " " + body

    mentions = re.findall(r"@(\w+)", text)

    for m in mentions:

        graph["nodes"].append({
            "id": m,
            "type": "Person"
        })

        graph["edges"].append({
            "source": issue_id,
            "target": m,
            "relation": "MENTIONED"
        })


with open("data/knowledge_graph.json", "w") as f:
    json.dump(graph, f, indent=2)

print("Knowledge graph with relationships created")

# Load comments
import os

if os.path.exists("data/comments.json"):

    with open("data/comments.json", "r") as f:
        comments = json.load(f)

    for comment in comments:

        commenter = comment["user"]["login"]
        issue_url = comment["issue_url"]

        issue_id = issue_url.split("/")[-1]

        graph["nodes"].append({
            "id": commenter,
            "type": "Person"
        })

        graph["edges"].append({
            "source": commenter,
            "target": issue_id,
            "relation": "COMMENTED_ON"
        })

# Remove duplicate nodes
unique_nodes = {}
for node in graph["nodes"]:
    unique_nodes[node["id"]] = node

graph["nodes"] = list(unique_nodes.values())