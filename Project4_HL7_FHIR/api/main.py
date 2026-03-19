import sys
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Move up 3 levels to reach ProjMain
root_dir = Path(__file__).resolve().parent.parent.parent

# 2. Add ProjMain to the search path
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from Project1_HL7_Parser.parser import hl7_updated_parser
from Project3_HL7_Database.db import crud, database
from Project3_HL7_Database.db.models import FHIRResource

from fhir.converter import (
    hl7_to_fhir_patient,
    hl7_to_fhir_encounter,
    build_fhir_bundle
)


class HL7Request(BaseModel):
    message: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Project 4 HL7 FHIR Parser API Running"}

"""
@app.post("/hl7-to-fhir")
def convert_patient(request: HL7Request):
    parsed = hl7_updated_parser.parse_hl7(request.message)
    print("Parsed HL7:", parsed)
    fhir = hl7_to_fhir_patient(parsed)
    return fhir
""" 

"""
@app.post("/hl7-to-fhir")
def convert(request: HL7Request):
    message = request.message
    message = message.replace("\\n", "\n")

    parsed = hl7_updated_parser.parse_hl7(message)

    patient = hl7_to_fhir_patient(parsed)
    encounter = hl7_to_fhir_encounter(parsed)

    return {
        "patient": patient,
        "encounter": encounter
    }
"""

@app.post("/hl7-to-fhir")
def convert(request: HL7Request):
    message = request.message
    message = message.replace("\\n", "\n")

    parsed = hl7_updated_parser.parse_hl7(message)

    patient = hl7_to_fhir_patient(parsed)
    encounter = hl7_to_fhir_encounter(parsed)

    bundle = build_fhir_bundle(patient, encounter)

    #Save FHIR Bundle to Database
    mydb = database.SessionLocal()
    crud.save_fhir_bundle(mydb, bundle)

    return bundle


@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    mydb = database.SessionLocal()

    result = mydb.query(FHIRResource).filter(
        FHIRResource.resource_type == "Patient",
        FHIRResource.resource_id == patient_id
    ).first()

    return result.data if result else {"error": "Not found"}