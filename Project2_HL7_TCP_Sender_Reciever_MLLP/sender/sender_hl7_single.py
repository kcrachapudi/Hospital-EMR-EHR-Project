import socket

HOST = "127.0.0.1"
PORT = 5000

START_BLOCK = b'\x0b'
END_BLOCK = b'\x1c'
CARRIAGE_RETURN = b'\x0d'

with open("../messages/sample.hl7", "r") as file:
    message = file.read()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

framed_message = START_BLOCK + message.encode() + END_BLOCK + CARRIAGE_RETURN

client.sendall(framed_message)
print("HL7 message sent!")

# Receive ACK
ack_data = client.recv(4096)

ack = ack_data.strip(START_BLOCK).strip(END_BLOCK).strip(CARRIAGE_RETURN)

print("\n--- ACK RECEIVED ---")
print(ack.decode())

client.close()