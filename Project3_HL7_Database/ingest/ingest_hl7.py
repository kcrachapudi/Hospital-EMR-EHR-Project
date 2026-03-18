import sys
from pathlib import Path

# 1. Move up 3 levels to reach ProjMain
root_dir = Path(__file__).resolve().parent.parent.parent

# 2. Add ProjMain to the search path
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

# 3. Import using the full path from ProjMain
from Project1_HL7_Parser.parser import hl7_parser

from Project3_HL7_Database.db.database import SessionLocal
from Project3_HL7_Database.db.crud import create_patient, create_visit, store_raw_message

def extract_patient(parsed):
    pid = parsed.get("PID", [])

    name = pid[4].split("^") if len(pid) > 4 else ["", ""]

    return {
        "patient_id": pid[2] if len(pid) > 2 else "",
        "first_name": name[1] if len(name) > 1 else "",
        "last_name": name[0] if len(name) > 0 else "",
        "dob": pid[6] if len(pid) > 6 else "",
        "gender": pid[7] if len(pid) > 7 else "",
    }


def extract_visit(parsed):
    pv1 = parsed.get("PV1", [])

    return {
        "patient_id": parsed.get("PID", [None, None, ""])[2],
        "visit_type": pv1[1] if len(pv1) > 1 else "",
        "location": pv1[2] if len(pv1) > 2 else "",
    }


def ingest_message(message):
    db = SessionLocal()

    store_raw_message(db, message)

    parsed = hl7_parser.parse_hl7(message)

    patient_data = extract_patient(parsed)
    visit_data = extract_visit(parsed)

    create_patient(db, patient_data)
    create_visit(db, visit_data)

    db.close()