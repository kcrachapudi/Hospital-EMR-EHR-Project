import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

# 1. Move up 3 levels to reach ProjMain
root_dir = Path(__file__).resolve().parent.parent.parent

# 2. Add ProjMain to the search path
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from Project1_HL7_Parser.parser.hl7_updated_parser import parse_hl7
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
    return {"message": "Project 4 Pure API Running"}

@app.post("/hl7-raw")
async def raw_hl7(message: str = Body(..., media_type="text/plain")):
    parsed = parse_hl7(message)

    patient = hl7_to_fhir_patient(parsed)
    encounter = hl7_to_fhir_encounter(parsed)
    bundle = build_fhir_bundle(patient, encounter)

    #Save FHIR Bundle to Database
    mydb = database.SessionLocal()
    crud.save_fhir_bundle(mydb, bundle)

    return bundle


@app.get("/patients")
def get_patients(name:str=None, gender:str=None, birthDate:str=None):
    mydb = database.SessionLocal()
    query = mydb.query(FHIRResource).filter(FHIRResource.resource_type == "Patient")

    if name:
        query = query.filter(FHIRResource.data["name"][0]["given"][0].astext.ilike(f"%{name}%"))
    if gender:
        query = query.filter(FHIRResource.data["gender"].astext == gender)
    if birthDate:
        query = query.filter(FHIRResource.data["birthDate"].astext == birthDate)

    results = query.all()
    return [result.data for result in results]


@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    mydb = database.SessionLocal()

    result = mydb.query(FHIRResource).filter(
        FHIRResource.resource_type == "Patient",
        FHIRResource.resource_id == patient_id
    ).first()
    if result:
        return result.data
    else: 
        raise HTTPException(status_code=404, detail="Patient not found")


@app.put("/patients/{patient_id}")
def update_patient(patient_id: str, updated_data: dict):
    mydb = database.SessionLocal()

    resource = mydb.query(FHIRResource).filter(
        FHIRResource.resource_type == "Patient",
        FHIRResource.resource_id == patient_id
    ).first()

    if not resource:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    resource.data = updated_data
    mydb.commit()

    return {"message": "Patient fully updated"}


@app.patch("/patients/{patient_id}")
def patch_patient(patient_id: str, updates: dict):
    mydb = database.SessionLocal()

    resource = mydb.query(FHIRResource).filter(
        FHIRResource.resource_type == "Patient",
        FHIRResource.resource_id == patient_id
    ).first()

    if not resource:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    resource.data.update(updates)
    mydb.commit()
    return {"message": "Patient partially updated"}


@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: str):
    mydb = database.SessionLocal()

    resource = mydb.query(FHIRResource).filter(
        FHIRResource.resource_type == "Patient",
        FHIRResource.resource_id == patient_id
    ).first()

    if not resource:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    mydb.delete(resource)
    mydb.commit()
    return {"message": "Patient deleted"}