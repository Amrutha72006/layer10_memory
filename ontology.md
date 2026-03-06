DATASET
GitHub Issues Dataset (Flask Repository Snapshot)

ENTITIES USED
1. Person
2. Issue
3. Repository
4. Comment
5. Label

CLAIMS / RELATIONSHIPS
1. OPENED        (Person → Issue)
2. COMMENTED_ON  (Person → Issue)
3. ASSIGNED_TO   (Issue → Person)
4. CLOSED        (Person → Issue)
5. LABELED_AS    (Issue → Label)
6. MENTIONED     (Person → Person or Issue)

EVIDENCE MODEL
Each relationship (claim) must contain:
- source_id
- text_excerpt
- timestamp