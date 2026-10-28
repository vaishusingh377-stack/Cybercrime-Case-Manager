
import json
import os
import datetime
FILE_NAME = "cases.json"


def load_cases():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_cases(cases):
    with open(FILE_NAME, "w") as file:
        json.dump(cases, file, indent=4)


def register_case():
    cases = load_cases()

    print("\n--- Register New Case ---")
    case_id = input("Enter Case ID: ").strip()

    if any(case["case_id"] == case_id for case in cases):
        print("This Case ID already exists!")
        return

    case_title = input("Enter Case Title: ").strip()
    crime_type = input("Enter Crime Type: ").strip()

    if not case_id or not case_title or not crime_type:
        print("All fields are required.")
        return

    case = {
        "case_id": case_id,
        "case_title": case_title,
        "crime_type": crime_type
    }

    cases.append(case)
    save_cases(cases)

    print("\nCase saved successfully!")


import hashlib


def analyze_evidence():
    file_path = input("\nEnter the path of the evidence file: ").strip()
    file_path = file_path.strip('"')

    if not os.path.isfile(file_path):
        print("File not found. Please check the path.")
        return

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    print("\n--- Evidence Analysis Report ---")
    print("File Name:", os.path.basename(file_path))
    print("SHA-256 Hash:", sha256.hexdigest())
    print("Keep this hash to verify file integrity later.")

def register_evidence():
    import hashlib
    import os

    cases = load_cases()

    case_id = input("Enter the Case ID: ").strip()

    case_exists = any(
        case["case_id"] == case_id for case in cases
    )

    if not case_exists:
        print("Case ID not found. Register the case first.")
        return

    file_path = input("Enter evidence file path: ").strip().strip('"')

    if not os.path.isfile(file_path):
        print("Evidence file not found.")
        return

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    evidence_hash = sha256.hexdigest()

    evidence_record = {
        "case_id": case_id,
        "evidence_file": os.path.basename(file_path),
        "sha256": evidence_hash
    }

    evidence_file = "evidence_registry.json"

    if os.path.exists(evidence_file):
        with open(evidence_file, "r") as file:
            evidence_records = json.load(file)
    else:
        evidence_records = []

    evidence_records.append(evidence_record)

    with open(evidence_file, "w") as file:
        json.dump(evidence_records, file, indent=4)

    print("Evidence details saved successfully!")

    print("\n--- EVIDENCE REGISTERED ---")
    print("Case ID:", case_id)
    print("Evidence File:", os.path.basename(file_path))
    print("SHA-256:", evidence_hash)

def view_evidence():
    evidence_file = "evidence_registry.json"

    if not os.path.exists(evidence_file):
        print("\nNo evidence registered yet.")
        return

    with open(evidence_file, "r") as file:
        evidence_records = json.load(file)

    if not evidence_records:
        print("\nNo evidence registered yet.")
        return

    print("\n--- REGISTERED DIGITAL EVIDENCE ---")

    for evidence in evidence_records:
        print("\n-------------------------")
        print("Case ID:", evidence["case_id"])
        print("Evidence File:", evidence["evidence_file"])
        print("SHA-256:", evidence["sha256"])

def view_cases():
    cases = load_cases()

    if not cases:
        print("\nNo cases registered yet.")
        return

    for case in cases:
        print("\n-------------------------")
        print("Case ID:", case["case_id"])
        print("Case Title:", case["case_title"])
        print("Crime Type:", case["crime_type"])


def calculate_file_hash(file_path):
    import hashlib

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()

def verify_evidence():
    evidence_file = "evidence_registry.json"

    if not os.path.exists(evidence_file):
        print("No registered evidence found.")
        return

    with open(evidence_file, "r") as file:
        evidence_records = json.load(file)

    if not evidence_records:
        print("No registered evidence found.")
        return

    case_id = input("Enter Case ID: ").strip()
    file_name = input("Enter evidence file path: ").strip().strip('"')

    if not os.path.isfile(file_name):
        print("Evidence file not found.")
        return

    matching_record = None

    for record in evidence_records:
        if (record["case_id"] == case_id and
                record["evidence_file"] == os.path.basename(file_name)):
            matching_record = record
            break

    if matching_record is None:
        print("No matching registered evidence found.")
        return

    current_hash = calculate_file_hash(file_name)

    if current_hash == matching_record["sha256"]:
        print("INTEGRITY VERIFIED: Evidence file is unchanged.")
    else:
        print("WARNING: Evidence file has been modified!")

def search_case():
    cases = load_cases()

    if not cases:
        print("No cases registered yet.")
        return

    search_id = input("Enter Case ID to search: ").strip()

    for case in cases:
        if case["case_id"].lower() == search_id.lower():
            print("\n--- CASE FOUND ---")
            print("Case ID:", case["case_id"])
            print("Case Title:", case["case_title"])
            print("Crime Type:", case["crime_type"])
            return

    print("No case found with this Case ID.")

def add_investigation_note():
    cases = load_cases()

    if not cases:
        print("No cases registered yet.")
        return

    case_id = input("Enter Case ID: ").strip()

    case = next(
        (item for item in cases if item["case_id"].lower() == case_id.lower()),
        None
    )

    if case is None:
        print("Case ID not found.")
        return

    note = input("Enter investigation note: ").strip()

    if not note:
        print("Note cannot be empty.")
        return

    notes_file = "investigation_notes.json"

    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            notes = json.load(file)
    else:
        notes = []

    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes.append({
        "case_id": case["case_id"],
        "note": note,
        "timestamp": timestamp
    })


    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=4)

    print("Investigation note saved successfully!")

def view_investigation_notes():
    notes_file = "investigation_notes.json"

    if not os.path.exists(notes_file):
        print("No investigation notes found.")
        return

    with open(notes_file, "r") as file:
        notes = json.load(file)

    if not notes:
        print("No investigation notes found.")
        return

    case_id = input("Enter Case ID to view notes: ").strip()

    matching_notes = [
        item for item in notes
        if item["case_id"].lower() == case_id.lower()
    ]

    if not matching_notes:
        print("No notes found for this Case ID.")
        return

    print("\n--- INVESTIGATION NOTES ---")

    for index, item in enumerate(matching_notes, start=1):
        print(f"\nNote {index}:")
        print(item["note"])
        print("Date & Time:", item.get("timestamp", "Not recorded"))

while True:
    print("\n========================================")
    print("CYBERCRIME INVESTIGATION CASE MANAGER")
    print("========================================")
    print("1. Register a New Case")
    print("2. View All Cases")
    print("3. Analyze Evidence File")
    print("4. Register Digital Evidence")
    print("5. View Registered Evidence")
    print("6. Verify Evidence Integrity")
    print("7. Search Case by Case ID")
    print("8. Add Investigation Note")
    print("9. View Investigation Notes")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ").strip()

    if choice == "1":
        register_case()
    elif choice == "2":
        view_cases()
    elif choice == "3":
        print("\nStarting Evidence Analyzer...")
        os.system("python evidence.py")
    elif choice == "4":
        register_evidence()
    elif choice == "5":
        view_evidence()
        
    elif choice == "6":
        verify_evidence()
    elif choice == "7":
        search_case()
    elif choice == "8":
        add_investigation_note()
    elif choice == "9":
        view_investigation_notes()
    elif choice == "10":
        print("Exiting Case Manager...")
        break
    else:
        print("Invalid choice. Please select 1-10.")





    


