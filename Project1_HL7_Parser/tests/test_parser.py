from parser import h17_parser

def test_parser():
    message1 = "MSH|^~\n|HOSPITAL|LAB|EHR|HOSPITAL|202101011230||ADT^A01|123456|P|2.3"
    message = "PID|1||123||DOE^JOHN"

    result = h17_parser.parse_h17(message)
    
    print(result["PID"])
    
    assert result["PID"][2] == "123"