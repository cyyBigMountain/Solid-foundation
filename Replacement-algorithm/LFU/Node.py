class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        val = f"{self.key}: {self.value}"
        return val

    def __repr__(self):
        val = f"{self.key}: {self.value}"
        return val
