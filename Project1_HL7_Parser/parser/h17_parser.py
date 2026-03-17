def parse_h17(message:str):
    segments = message.strip().split('\n')
    parsed = {}
    for segment in segments:
        fields = segment.split('|')
        segment_type = fields[0]

        parsed[segment_type] = fields[1:]
    return parsed