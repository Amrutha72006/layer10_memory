# Layer10 Memory — Knowledge Graph Builder

## Overview

Layer10 Memory is a Python-based project that extracts entities from textual data and builds a **knowledge graph** representing relationships between those entities.

The system performs **basic NLP processing, entity extraction, graph construction, visualization, and analytics** to understand how entities interact within a dataset.

This project demonstrates concepts from:

* Natural Language Processing (NLP)
* Knowledge Graph Construction
* Graph Analytics
* Data Processing using Python

---

## Features

### Entity Extraction

Extracts entities from textual data using **spaCy NLP models**.

### Knowledge Graph Construction

Builds a graph connecting related entities using **NetworkX**.

### Graph Visualization

Visualizes entity relationships using **Matplotlib**.

### Graph Analytics

Computes useful statistics such as:

* Number of nodes
* Number of edges
* Most connected entities

### Comment Collection

Supports collecting comments related to issues in the dataset.

---

## Technologies Used

* Python
* spaCy
* NetworkX
* Matplotlib
* JSON
* Pandas

---

## Project Structure

```
layer10_memory
│
├── data/              # Input and processed data
├── extraction/        # Entity extraction code
├── graph/             # Graph creation and analysis
├── scripts/           # Data collection scripts
├── retrieval/         # Retrieval logic
├── ui/                # Visualization or UI components
│
├── README.md
├── requirements.txt
└── .gitignore
└── ontology.md

```

---

## Installation

Clone the repository:

```
git clone https://github.com/Amrutha72006/layer10_memory.git
cd layer10_memory
```

Create virtual environment:

```
python -m venv venv
```

Activate the environment (Windows):

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Download the spaCy model:

```
python -m spacy download en_core_web_sm
```

---

## How to Run

### 1. Collect Data

```
python scripts/collect_data.py
```

---

### 2. Extract Entities

```
python extraction/extract_entities.py
```

---

### 3. Build Knowledge Graph

```
python graph/build_graph.py
```

---

### 4. Run Graph Analytics

```
python graph/analyze_graph.py
```

---

### 5. Visualize the Graph

```
python graph/visualize_graph.py
```

This generates a **network graph visualization showing relationships between extracted entities.**

---

## Output

The system generates:

* `entities.json` — Extracted entities
* `graph.png` — Visual knowledge graph
* Graph analytics printed in the terminal

---

## Example Use Case

Given a dataset of textual claims or issues, the system can identify entities such as **people, repositories, labels, and issues**, and connect them inside a knowledge graph.

Example relationships:

```
Person → OPENED → Issue
Issue → LABELED_AS → Bug
Issue → ASSIGNED_TO → Developer
```

This helps visualize how entities interact within a dataset.

---

## Future Improvements

Possible extensions include:

* Interactive graph visualization
* Web interface for querying the graph
* Advanced relation extraction
* Integration with larger datasets

---

## Author

Developed as a project exploring **NLP, knowledge graphs, and graph analytics using Python**.
