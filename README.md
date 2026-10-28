# Cybercrime Investigation Case Manager

## About the Project
The Cybercrime Investigation Case Manager is a beginner-friendly Python project designed to manage cybercrime cases and digital evidence. It helps organize case details, register evidence files, verify evidence integrity, and maintain investigation notes.

## Features
- **Case Management:** Register and view cybercrime cases.
- **Evidence Registration:** Store digital evidence details linked to a case ID.
- **SHA-256 Hashing:** Generate a unique hash for evidence files.
- **Evidence Integrity Verification:** Detect whether a registered evidence file has been modified.
- **Case Search:** Search cases using a Case ID.
- **Investigation Notes:** Add and view notes with date and time.
- **JSON Storage:** Save case information, evidence records, and investigation notes in JSON files.

## Technologies Used
- Python
- JSON
- SHA-256 Hashing
- VS Code

## Project Files
- `main.py` — Main application and menu system.
- `evidence.py` — Standalone evidence hashing tool.
- `sample_evidence.txt` — Sample file for testing evidence integrity.
- `cases.json` — Stores registered cases.
- `evidence_registry.json` — Stores registered evidence records and hashes.
- `investigation_notes.json` — Stores investigation notes and timestamps.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python main.py
```

6. Follow the menu options to manage cases and digital evidence.

To run the standalone evidence hashing tool:

```bash
python evidence.py
```

## Learning Outcomes
This project helped me practise Python programming, file handling, JSON data storage, SHA-256 hashing, evidence integrity verification, and basic digital forensics concepts.

## Disclaimer
This project is intended for educational purposes and uses sample data. Use it only with files you are authorized to access and analyze.

## Author
Cybersecurity Graduate | Aspiring Cybersecurity and Digital Forensics Professional
