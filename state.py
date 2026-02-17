# state.py

from dataclasses import dataclass, field
from typing import Dict, Any
import uuid

@dataclass
class EvoState:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    generation: int = 0
    variables: Dict[str, Any] = field(default_factory=dict)

    def snapshot(self):
        return {
            "id": self.id,
            "generation": self.generation,
            "variables": self.variables.copy()
        }