
# Library Management System

 - A completed, production-ready Command Line Interface (CLI) application built with Python to manage books, track lending status, and handle persistence using JSON data stores. 
 - This project was built following OOP standard, and isolated environment environments(optional).

# Key Technical Features

 - Virtual Environments (venv): Dependencies and execution environments are completely isolated, an optional choice for user
 - Core OOP Blueprinting: Zero linear script processing, cleanly works with lowest time complexity.
 - File I/O & Error Catching: Uses native json data streaming combined with defensive programming to catch missing data stores gracefully without system failure.

# Installation & Setup

Follow these sequential steps to fire up the system inside your terminal:
1. Set Up the Isolated Environment
Navigate into your root project directory and initialize a clean .venv:
```bash
python -m venv .venv
```
2. Activate the Virtual Environment
Activate your environment space before execution:
 - Window (CMD/PS):
```bash
.venv\Scripts\activate
```
 - Mac/Linux:
```bash
source .venv/bin/activate
```
3. Run the Application:
Execute the main script via your python engine:
```bash
python main.py
```
or if you have python3
```bash
python3 main.py
```

# Application Features & Capabilities

When you initialize the application, you can easily control your workspace via a menu:
1. View All Books: Loops through inventory to display individual statuses using string overriding (__str__).
2. Add New Books: Captures entries while enforcing ISBN validation and catching input type errors (ValueError).
3. Search Library: Queries the memory list instantly targeting unique ISBN markers.
4. Process Borrowing: Validates availability, and returning error feedback if items are missing or already checked out.
5. Auto-Persistence on Exit: Automatically dumps object data mappings into `library_data.json` before closing out completely.

# Project architecture
```text
├── .venv/                  # Isolated Python environment
├── .gitignore			# Gitignore cache
├── README.md			# Instructions
├── book.py                 # Defines the Book data structure & representations
├── library.py              # Manages lists of Book objects, validation, and JSON I/O
└── main.py                 # Direct entry point containing the loop-driven CLI Menu
```

