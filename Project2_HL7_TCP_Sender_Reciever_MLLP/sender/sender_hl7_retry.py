import socket
import time

HOST = "127.0.0.1"
PORT = 5000

START_BLOCK = b'\x0b'
END_BLOCK = b'\x1c'
CARRIAGE_RETURN = b'\x0d'

MAX_RETRIES = 3
TIMEOUT = 5  # seconds

with open("../messages/sample.hl7", "r") as file:
    message = file.read()

framed_message = START_BLOCK + message.encode() + END_BLOCK + CARRIAGE_RETURN

def send_message():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(TIMEOUT)

    try:
        client.connect((HOST, PORT))
        client.sendall(framed_message)

        ack_data = client.recv(4096)

        ack = ack_data.strip(START_BLOCK).strip(END_BLOCK).strip(CARRIAGE_RETURN).decode()

        print("\n--- ACK RECEIVED ---")
        print(ack)

        if "MSA|AA" in ack:
            print("✅ Message delivered successfully")
            return True
        else:
            print("⚠️ Negative ACK received")
            return False

    except socket.timeout:
        print("⏱️ Timeout waiting for ACK")
        return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

    finally:
        client.close()


# Retry loop
for attempt in range(1, MAX_RETRIES + 1):
    print(f"\nAttempt {attempt}...")

    success = send_message()

    if success:
        break
    else:
        print("Retrying...")
        time.sleep(2)

if not success:
    print("❌ Message failed after retries")