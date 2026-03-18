from sqlalchemy import Column, Integer, String 
from database import Base

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
    gender = Column(String)


class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String)
    visit_type = Column(String)
    location = Column(String)

class HL7Message(Base):
    __tablename__ = "hl7_messages"

    id = Column(Integer, primary_key=True, index=True)
    raw_message = Column(String)