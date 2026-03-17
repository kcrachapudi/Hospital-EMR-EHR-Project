from hl7_parser import parse_hl7, hl7_to_json

def parse_local():
    message1 = "MSH|^~\n|HOSPITAL|LAB|EHR|HOSPITAL|202101011230||ADT^A01|123456|P|2.3"
    message = "PID|1||123||DOE^JOHN"

    result = parse_h17(message)
    
    print(result["PID"])
    
    print(result["PID"][2])

def get_sample_message():
    with open("../sample_messages/admit.hl7") as f:
        message = f.read()
    return message

def parse_message():
    message = get_sample_message()

    result = parse_hl7(message)
    return result


def parse_json():
    parsed = parse_message()
    return hl7_to_json(parsed)


#parse_local()
#print(parse_message())
print(parse_json())