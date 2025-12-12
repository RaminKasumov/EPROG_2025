import random
from collections import defaultdict

class CharMarkov:
    def __init__(self):
        self.model = defaultdict(list)

    def train(self, text):
        for i in range(len(text) - 2):
            key = (text[i], text[i+1])
            self.model[key].append(text[i+2])

    def generate(self, length=500, seed=None):
        if seed is None:
            seed = random.choice(list(self.model.keys()))
        if isinstance(seed, str):
            if len(seed) != 2:
                raise ValueError("Seed string must have length 2")
            state = (seed[0], seed[1])
        else:
            state = seed
        out = [state[0], state[1]]
        for _ in range(length - 2):
            choices = self.model.get(state)
            if not choices:
                state = random.choice(list(self.model.keys()))
                out.append(state[1])
                continue
            next_char = random.choice(choices)
            out.append(next_char)
            state = (state[1], next_char)
        return "".join(out)

def read_text(path):
    with open(path, "r") as f:
        return f.read()

text = read_text("data/data.txt")
mg = CharMarkov()
mg.train(text)
random.seed(42)
generated = mg.generate(length=400)
print("---- Generated text (first 400 chars) ----")
print(generated)