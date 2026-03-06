import json

with open("data/knowledge_graph.json", "r") as f:
    graph = json.load(f)

nodes = graph["nodes"]
edges = graph["edges"]

print("Total Nodes:", len(nodes))
print("Total Relationships:", len(edges))

# Most active issue creator
users = {}
for e in edges:
    if e["relation"] == "OPENED":
        users[e["source"]] = users.get(e["source"], 0) + 1

if users:
    top_user = max(users, key=users.get)
    print("Most Active Issue Creator:", top_user)

# Most common label
labels = {}
for e in edges:
    if e["relation"] == "LABELED_AS":
        labels[e["target"]] = labels.get(e["target"], 0) + 1

if labels:
    top_label = max(labels, key=labels.get)
    print("Most Common Label:", top_label)

# Most mentioned developer
mentions = {}

for e in edges:
    if e["relation"] == "MENTIONED":
        mentions[e["target"]] = mentions.get(e["target"], 0) + 1

if mentions:
    top_mention = max(mentions, key=mentions.get)
    print("Most Mentioned Developer:", top_mention)