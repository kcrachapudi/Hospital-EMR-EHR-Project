def parse_hl7(message: str):
    # 🔥 FIX: Convert escaped newlines to real newlines
    message = message.replace("\\n", "\n")

    segments = message.strip().split("\n")
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

    return parsed