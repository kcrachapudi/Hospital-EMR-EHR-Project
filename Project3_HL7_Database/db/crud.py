import sys
from pathlib import Path
from sqlalchemy.orm import Session

# 1. Get the absolute path to the folder containing THIS script
script_dir = Path(__file__).resolve().parent

# 2. Add that folder to the front of Python's search path
if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir))

from Project3_HL7_Database.db.models import Patient, Visit, FHIRResource

def create_patient(db, data):
    patient = Patient(**data)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def create_visit(db, data):
    visit = Visit(**data)
    db.add(visit)
    db.commit()
    db.refresh(visit)
    return visit


def store_raw_message(db, message: str):
    hl7_msg = HL7Message(raw_message=message)
    db.add(hl7_msg)
    db.commit()
    db.refresh(hl7_msg)
    return hl7_msg


def save_fhir_bundle(db: Session, bundle: dict):
    for entry in bundle.get("entry", []):
        resource = entry.get("resource", {})
        
        db_resource = FHIRResource(
            resource_type=resource.get("resourceType"),
            resource_id=resource.get("id"),
            data=resource
        )
        
        db.add(db_resource)
    
    db.commit()