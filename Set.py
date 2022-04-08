class Set:

    def __init__(self, *args):
        if len(args) == 0:
            self.cardinal = 0
            self.elements = []

        if len(args) == 1:
            if isinstance(args[0], list):
                self.cardinal = 0
                self.elements = []
                self.fill(args[0])

    def fill(self, elements):
        for i in range(len(elements)):
            self.add(elements[i])

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
            self.cardinal += 1

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
            self.cardinal -= 1

    def union(self):
        pass

    def intersect(self):
        pass

    def contains(self, e):
        for i in range(len(self.elements)):
            if e == self.elements[i]:
                return True
        return False

    def minus(self, inset):
        outset = Set()

        for i in range(len(max({self.cardinal, inset.cardinal}))):
            if self.elements[i] in inset.elements[i]:
                outset.elements.append(self.elements[i])
        return outset

    def tostring(self):
        return str(self.elements).replace("[", "{").replace("]", "}") + "." + str(self.cardinal)

    def display(self):
        print(self.tostring())