# evolution.py

def evolve(state):
    """
    Simple mutation rule:
    Increment numeric variables by 1.
    """

    new_vars = {}

    for k, v in state.variables.items():
        if isinstance(v, (int, float)):
            new_vars[k] = v + 1
        else:
            new_vars[k] = v

    state.variables = new_vars
    state.generation += 1

    return state