from fastapi import FastAPI, Body
from pydantic import BaseModel
from parser.hl7_parser import parse_hl7, hl7_to_json

app = FastAPI()

class HL7Request(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "HL7 Parser API Running"}

@app.post("/parse_hl7")
def parse_message(message: str=Body(..., media_type="text/plain")):
    parsed = parse_hl7(message)
    return hl7_to_json(parsed)