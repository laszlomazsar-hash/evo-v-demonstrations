# ledger.py

import json
from datetime import datetime

class Ledger:

    def __init__(self):
        self.records = []

    def record(self, state_snapshot):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "state": state_snapshot
        }
        self.records.append(entry)

    def export(self, filename="ledger.json"):
        with open(filename, "w") as f:
            json.dump(self.records, f, indent=2)