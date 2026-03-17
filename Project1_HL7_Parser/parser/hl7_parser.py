def parse_hl7(message:str):
    segments = message.strip().split('\n')
    parsed = {}
    for segment in segments:
        fields = segment.split('|')
        segment_type = fields[0]

        parsed[segment_type] = fields[1:]
    return parsed


def hl7_to_json(parsed):
    result = {}
    #Patient Info PID
    if 'PID' in parsed:
        pid = parsed['PID']
        name = pid[4].split('^') if len(pid) > 4 else ['', '']

        result['patient'] = {
            "id": pid[2],
            "first_name": name[1] if len(name) > 1 else '',
            "last_name": name[0] if len(name) > 0 else '',
            "dob": pid[6],
            "gender": pid[7]
        }
    return result