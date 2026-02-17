# governance.py

class Governance:

    def __init__(self, max_generations=100):
        self.max_generations = max_generations
        self.interrupted = False

    def validate(self, state):
        if state.generation > self.max_generations:
            raise Exception("Governance limit exceeded.")

        for value in state.variables.values():
            if isinstance(value, (int, float)) and value > 1000:
                raise Exception("Variable overflow detected.")

    def interrupt(self):
        self.interrupted = True