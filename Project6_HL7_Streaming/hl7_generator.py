import time
import random
import requests

URL = "http://127.0.0.1:8000/hl7-raw"

patients = [
    ("2001", "Rice", "Condy", "19850505", "F"),
    ("2002", "Whetstone", "Bret", "19900202", "M"),
    ("2003", "Falck", "Greg", "19781212", "M"),
]


def generate_message():
    p = random.choice(patients)

    message = f"""MSH|^~\&|App|Fac|RecApp|RecFac|202403161200||ADT^A01|MSG{random.randint(3000,9999)}|P|2.3
PID|1||{p[0]}||{p[1]}^{p[2]}||{p[3]}|{p[4]}
PV1|1|I|ER"""
    return message


while True:
    hl7_message = generate_message()
    print(f"Generated HL7 Message:\n{hl7_message}\n")
    response = requests.post(URL, data=hl7_message, headers={"Content-Type": "text/plain"})
    print(f"HL7 API Response: {response.status_code} - {response.text}\n")
    time.sleep(2)


