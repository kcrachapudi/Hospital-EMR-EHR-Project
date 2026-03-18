def hl7_to_fhir_patient(parsed_hl7: dict):
    pid = parsed_hl7.get("PID", {})

    return {
        "resourceType": "Patient",
        "id": pid.get("patient_id"),
        "name": [
            {
                "family": pid.get("last_name"),
                "given": [pid.get("first_name")]
            }
        ],
        "gender": map_gender(pid.get("gender")),
        "birthDate": format_date(pid.get("dob"))
    }


def map_gender(gender):
    if gender == "M":
        return "male"
    elif gender == "F":
        return "female"
    return "unknown"


def format_date(date_str):
    # HL7: YYYYMMDD → FHIR: YYYY-MM-DD
    if not date_str:
        return None
    return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"