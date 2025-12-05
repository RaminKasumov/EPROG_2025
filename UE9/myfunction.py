class MyFunction:
    def __init__(self, func, domain_start, domain_end):
        self.func = func
        self.a = domain_start
        self.b = domain_end

    def __call__(self, x):
        if x < self.a or x > self.b:
            raise ValueError(f"Value {x} is outside the domain [{self.a}, {self.b}].")
        return self.func(x)

    def __repr__(self):
        return f"MyFunction(domain=[{self.a}, {self.b}])"