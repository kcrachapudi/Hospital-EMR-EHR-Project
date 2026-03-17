import socket 
HOST = "127.0.0.1"
PORT = 5000

START_BLOCK = b'\x0b'
END_BLOCK = b'\x1c'
CARRIAGE_RETURN = b'\x0d'

with open("../messages/sample.hl7", "r") as file:
    hl7_message = file.read()

hl7_encoded_message = hl7_message.encode('utf-8')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Add MLLP framing to the HL7 message
framed_message = START_BLOCK +  hl7_encoded_message + END_BLOCK + CARRIAGE_RETURN

client.sendall(framed_message)

print("HL7 Message sent to the receiver.")
client.close()