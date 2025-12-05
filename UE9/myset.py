class MySet:
    def __init__(self, data):
        self.items = []
        for element in data:
            if element not in self.items:
                self.items.append(element)

    def __add__(self, other):
        result = MySet(self.items)
        for element in other.items:
            if element not in result.items:
                result.items.append(element)
        return result

    def __sub__(self, other):
        result = [element for element in self.items if element not in other.items]
        return MySet(result)

    def add(self, a):
        if a not in self.items:
            self.items.append(a)

    def __repr__(self):
        return f"MySet({self.items})"