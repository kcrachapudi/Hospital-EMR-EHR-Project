# Healthcare Integration Lab

A complete simulation of hospital data interoperability using HL7 and FHIR.

## Projects

1. HL7 Parser
2. HL7 Simulator
3. Database Pipeline
4. HL7 → FHIR Converter
5. FHIR API
6. Mini Hospital System
7. Production Stack

## Architecture

Hospital → HL7 → Parser → DB → FHIR → API


# HL7 to FHIR Healthcare Data Pipeline

This project is a real-time healthcare data integration system that processes HL7 messages and converts them into FHIR resources.

It simulates how hospital systems exchange and transform patient data.

- Python
- FastAPI
- PostgreSQL
- HL7
- FHIR

# Pipeline Architecture
HL7 Message → Parser → Validator → FHIR Converter → Database → API

# Features
- HL7 message parsing (MSH, PID, PV1)
- Validation engine
- HL7 → FHIR conversion
- REST API (CRUD operations)
- Search & filtering
- Real-time message streaming
- Logging system (file + console)

## Example HL7 Input
MSH|^~\&|App|Fac|RecApp|RecFac|...
PID|1||1001||Smith^John||19850505|M
PV1|1|I|ER

MSH|^~\&|App|Fac|RecApp|RecFac|202403161200||ADT^A01|MSG00001|P|2.3
PID|1||1005||Reagan^Nancy||19850505|F
PV1|1|I|ER

MSH|^~\&|App|Fac|RecApp|RecFac|202403161201||ADT^A01|MSG00002|P|2.3
PID|1||1006||Doe^Jane||19900210|F
PV1|1|O|Clinic

MSH|^~\&|App|Fac|RecApp|RecFac|202403161202||ADT^A01|MSG00003|P|2.3
PID|1||1007||Brown^Charlie||19781225|M
PV1|1|I|ICU

MSH|^~\&|App|Fac|RecApp|RecFac|202403161200||ADT^A01|MSG00001|P|2.3
PID|1||1008||Bundy^Fred||19850505|M
PV1|1|I|ER


## FHIR Output
{
  "resourceType": "Patient",
  "name": [
    {
      "family": "Smith",
      "given": ["John"]
    }
  ]
}

# API Endpoints
POST /hl7-raw
GET /patients
GET /patients?name=Smith
GET /patients?gender=male
GET /patients?birthDate=1985-05-05
PUT /patients/{id}
PATCH /patients/{id}
DELETE /patients/{id}

# How to Run
pip install -r requirements.txt
uvicorn PureAPI:app --reload

Run the HL7 generator to simulate real-time hospital message flow.

# Logs
Logs are written to PureAPI.log for monitoring system activity.


# Project Casual Description

I built a healthcare data integration pipeline that processes HL7 messages and converts them into FHIR resources.

It includes a parser, validation layer, transformation into FHIR format, and storage in PostgreSQL. I also built REST APIs for querying patient data and added a streaming component to simulate real-time hospital message flow.

This project helped me understand how healthcare systems exchange and normalize data.

❓ “What’s special about it?”
Most projects are CRUD-based, but this one handles real-world data formats like HL7 and FHIR and simulates an actual integration pipeline used in healthcare systems.
🏁 Where you stand now
Learning → Building → Debugging → Integrating → Streaming → Logging → Packaging


# Job Roles 
HL7 developer
FHIR developer
Healthcare integration engineer
Interface engine HL7
Python FastAPI backend engineer
Healthcare backend engineer
