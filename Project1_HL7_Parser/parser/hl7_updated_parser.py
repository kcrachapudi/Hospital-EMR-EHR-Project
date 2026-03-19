def parse_hl7_old(message: str):
    # 🔥 FIX: Convert escaped newlines to real newlines
    #message = message.replace("\\n", "\n")
    #segments = message.strip().split("\n")
    segments = message.strip().splitlines()
    print(f"Segments: {segments}")  # Debugging output
    parsed = {}

    for segment in segments:
        fields = segment.split("|")
        segment_type = fields[0]

        if segment_type == "PID":
            # Safe extraction
            patient_id = fields[3] if len(fields) > 3 else None

            name_field = fields[5] if len(fields) > 5 else ""
            name_parts = name_field.split("^") if name_field else ["", ""]

            last_name = name_parts[0] if len(name_parts) > 0 else None
            first_name = name_parts[1] if len(name_parts) > 1 else None

            dob = fields[7] if len(fields) > 7 else None
            gender = fields[8] if len(fields) > 8 else None

            parsed["PID"] = {
                "patient_id": patient_id,
                "first_name": first_name,
                "last_name": last_name,
                "dob": dob,
                "gender": gender,
            }
        elif segment_type == "PV1":
            visit_type = fields[2] if len(fields) > 2 else None
            location = fields[3] if len(fields) > 3 else None

            parsed["PV1"] = {
                "visit_type": visit_type,
                "location": location
            }    

    return parsed


def parse_hl7(message: str):
    # 🔥 FIX: Convert escaped newlines to real newlines
    #message = message.replace("\\n", "\n")
    #segments = message.strip().split("\n")
    segments = message.strip().splitlines()
    print(f"Segments: {segments}")  # Debugging output
    parsed = {}

    for line in segments:
        line = line.strip()
        if not line:
            continue

        fields = line.split("|")
        segment_type = fields[0].strip().upper()
        print(f"Processing segment: {segment_type} with fields: {fields}")  # Debugging output
        
        if segment_type == "MSH":
            parsed["MSH"] = {
                "sending_app": fields[2],
                "message_type": fields[8]
            }
        elif segment_type == "PID":
            # Safe extraction
            patient_id = fields[3] if len(fields) > 3 else None

            name_field = fields[5] if len(fields) > 5 else ""
            name_parts = name_field.split("^") if name_field else ["", ""]

            last_name = name_parts[0] if len(name_parts) > 0 else None
            first_name = name_parts[1] if len(name_parts) > 1 else None

            dob = fields[7] if len(fields) > 7 else None
            gender = fields[8] if len(fields) > 8 else None

            parsed["PID"] = {
                "patient_id": patient_id,
                "first_name": first_name,
                "last_name": last_name,
                "dob": dob,
                "gender": gender,
            }
        elif segment_type == "PV1":
            visit_type = fields[2] if len(fields) > 2 else None
            location = fields[3] if len(fields) > 3 else None

            parsed["PV1"] = {
                "visit_type": visit_type,
                "location": location
            }    
    print(f"Final Parsed HL7 Message: {parsed}")  # Debugging output  
    return parsed


def validate_hl7(parsed: dict):
    if not parsed:
        raise ValueError("Empty or invalid HL7 message")

    # Required segments
    if "MSH" not in parsed:
        raise ValueError("Missing MSH segment")

    if "PID" not in parsed:
        raise ValueError("Missing PID segment")

    pid = parsed["PID"]

    # Required fields
    if not pid.get("patient_id"):
        raise ValueError("Missing patient ID")

    if not pid.get("first_name") or not pid.get("last_name"):
        raise ValueError("Missing patient name")

    if not pid.get("dob"):
        raise ValueError("Missing date of birth")

    if pid.get("gender") not in ["M", "F"]:
        raise ValueError("Invalid gender value")