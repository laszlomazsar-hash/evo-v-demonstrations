# main.py

from state import EvoState
from governance import Governance
from ledger import Ledger
from kernel import EvoKernel

if __name__ == "__main__":

    initial_state = EvoState(
        variables={
            "energy": 1,
            "knowledge": 5
        }
    )

    governance = Governance(max_generations=10)
    ledger = Ledger()

    kernel = EvoKernel(initial_state, governance, ledger)

    kernel.run()

    ledger.export()

    print("EVO-V v0.1 complete.")