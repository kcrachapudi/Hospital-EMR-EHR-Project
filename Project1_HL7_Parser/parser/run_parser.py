from h17_parser import parse_h17

def parse_message():
    with open("../sample_messages/admit.hl7") as f:
        message = f.read()

    result = parse_h17(message)
    print(result)


def parse_local():
    message1 = "MSH|^~\n|HOSPITAL|LAB|EHR|HOSPITAL|202101011230||ADT^A01|123456|P|2.3"
    message = "PID|1||123||DOE^JOHN"

    result = parse_h17(message)
    
    print(result["PID"])
    
    print(result["PID"][2])

parse_local()
parse_message()