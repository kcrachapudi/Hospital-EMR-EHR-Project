import sys
from pathlib import Path

# 1. Move up 3 levels to reach ProjMain
root_dir = Path(__file__).resolve().parent.parent.parent

# 2. Add ProjMain to the search path
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from Project1_HL7_Parser.parser.hl7_updated_parser import parse_hl7

msg = """MSH|^~\\&|App|Fac|RecApp|RecFac|202403161200||ADT^A01|MSG00001|P|2.3
PID|1||1001||Smith^John||19850505|M
"""

print(parse_hl7(msg))