import sys
from pathlib import Path

# 1. Move up 3 levels to reach ProjMain
root_dir = Path(__file__).resolve().parent.parent.parent

# 2. Add ProjMain to the search path
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from Project3_HL7_Database.ingest.ingest_hl7 import ingest_message

messagefile = str(root_dir.joinpath("Project2_HL7_TCP_Sender_Reciever_MLLP", "messages", "sample.hl7"))
with open(messagefile) as f:
    message = f.read()

ingest_message(message)

print("Inserted into DB!")