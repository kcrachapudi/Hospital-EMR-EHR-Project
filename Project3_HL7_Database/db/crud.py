import sys
from pathlib import Path

# 1. Get the absolute path to the folder containing THIS script
script_dir = Path(__file__).resolve().parent

# 2. Add that folder to the front of Python's search path
if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir))

import models

def create_patient(db, data):
    patient = models.Patient(**data)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def create_visit(db, data):
    visit = models.Visit(**data)
    db.add(visit)
    db.commit()
    db.refresh(visit)
    return visit


def store_raw_message(db, message: str):
    hl7_msg = models.HL7Message(raw_message=message)
    db.add(hl7_msg)
    db.commit()
    db.refresh(hl7_msg)
    return hl7_msg