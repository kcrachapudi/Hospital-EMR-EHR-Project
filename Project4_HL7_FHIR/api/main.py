import sys
from pathlib import Path
from pydantic import BaseModel

# 1. Move up 3 levels to reach ProjMain
root_dir = Path(__file__).resolve().parent.parent.parent

# 2. Add ProjMain to the search path
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from fastapi import FastAPI
from fhir.converter import hl7_to_fhir_patient
from Project1_HL7_Parser.parser import hl7_updated_parser

class HL7Request(BaseModel):
    message: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Project 4 HL7 FHIR Parser API Running"}


@app.post("/hl7-to-fhir")
def convert(request: HL7Request):
    parsed = hl7_updated_parser.parse_hl7(request.message)
    print("Parsed HL7:", parsed)
    fhir = hl7_to_fhir_patient(parsed)
    return fhir