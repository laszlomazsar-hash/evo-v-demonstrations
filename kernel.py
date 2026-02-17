# kernel.py

from evolution import evolve

class EvoKernel:

    def __init__(self, state, governance, ledger):
        self.state = state
        self.governance = governance
        self.ledger = ledger

    def step(self):
        if self.governance.interrupted:
            print("Kernel interrupted.")
            return False

        self.state = evolve(self.state)
        self.governance.validate(self.state)
        self.ledger.record(self.state.snapshot())

        return True

    def run(self):
        while self.step():
            pass