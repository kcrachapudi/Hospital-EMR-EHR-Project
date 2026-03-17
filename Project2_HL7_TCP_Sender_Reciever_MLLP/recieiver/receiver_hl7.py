import socket
import random

HOST = "127.0.0.1"
PORT = 5000

START_BLOCK = b'\x0b'
END_BLOCK = b'\x1c'
CARRIAGE_RETURN = b'\x0d'

def create_ack():
    if random.choice([True, False]):
        return "MSH|^~\\&|RECEIVER|HOSPITAL|SENDER|SYSTEM|202603081200||ACK^A01|1234|P|2.5\rMSA|AA|1234"
    else:
        return "MSH|^~\\&|RECEIVER|HOSPITAL|SENDER|SYSTEM|202603081200||ACK^A01|1234|P|2.5\rMSA|AE|1234"

def frame_message(message):
    return START_BLOCK + message.encode() + END_BLOCK + CARRIAGE_RETURN

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"HL7 Receiver running on {HOST}:{PORT}...")

while True:
    conn, addr = server.accept()
    print(f"\nConnected by {addr}")

    data = conn.recv(4096)

    if not data:
        conn.close()
        continue

    # Remove MLLP framing
    un_mllp_message = data.strip(START_BLOCK).strip(END_BLOCK).strip(CARRIAGE_RETURN)

    print("\n--- HL7 MESSAGE RECEIVED ---")
    print(un_mllp_message.decode())

    # Send ACK
    ack_message = create_ack()
    framed_ack = frame_message(ack_message)

    conn.sendall(framed_ack)
    print("\n--- ACK SENT ---")

    conn.close()