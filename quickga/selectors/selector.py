class Selector:

    def get_survivors(self, population):
        raise NotImplementedError(f"Selector {type(self).__name__} must implement the \"get_survivors\" method")

    def select_parent(self, population):
        raise NotImplementedError(f"Selector {type(self).__name__} must implement the \"select_parent\" method")
