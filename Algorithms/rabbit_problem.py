import random

class Warren:
    size: int
    pos: int  # \leq size
    guesses = 0
    insecure: bool

    def __init__(self, size: int, insecure=False):
        self.pos = random.randint(0, size - 1)
        self.size = size
        self.insecure = insecure

    def get_size(self):
        return self.size

    def guess(self, attempt: int):
        self.guesses += 1
        if attempt == self.pos:
            self.step()
            g = self.guesses
            self.guesses = 0
            return g
        else:
            self.step()
            return False

    def step(self):
        if (random.randint(0, 1) == 1 or self.pos == 0) and self.pos < self.size-1:
            self.pos += 1
        else:
            self.pos -= 1

    def print_pos(self):
        if self.insecure:
            print(self.pos)


def rabbit_search(warren: Warren):
    for i in range(warren.get_size()):  # Check each burrow once => warren.get_size() checks
        g = warren.guess(i)
        if g:
            return g
    for i in range(1 if warren.get_size() % 2 == 0 else 0, warren.get_size()):
        g = warren.guess(i)
        if g:
            return g
    return False