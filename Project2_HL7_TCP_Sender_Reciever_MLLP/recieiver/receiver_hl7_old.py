import socket
HOST = "127.0.0.1"
PORT = 5000

rec_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rec_server.bind((HOST, PORT))
rec_server.listen(1)

print(f"HL7 Receiver Running on {HOST}:{PORT}... ")
conn, addr = rec_server.accept()
print(f"Connection established with {addr}")

mllp_data = conn.recv(4096)

#Remove MLLP framing
un_mllp_message = mllp_data.strip(b'\x0b').strip(b'\x1c').strip(b'\x0d')
hl7_message = un_mllp_message.decode('utf-8')
print("Received HL7 Message:")
print(hl7_message)
conn.close()