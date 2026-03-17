from h17_parser import parse_h17

with open("../sample_messages/admit.hl7") as f:
    message = f.read()

result = parse_h17(message)
print(result)