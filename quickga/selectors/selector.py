class Selector:

    def __init__(self, population):
        pass

    def select_parent(self):
        raise NotImplementedError(f"Selector {type(self).__name__} must implement the \"select_parent\" method")
