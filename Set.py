class Set:
    def __init__(self, holes=None):
        if holes is None:
            self.cardinal = 0
            self.elements = []

        if holes == 1:
            self.cardinal = 0
            self.fill(holes)

    def display(self):
        print(str(self.elements).replace("[", "{").replace("]", "}") + "." + str(self.cardinal))

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

    def minus(self, inset):
        outset = Set()

        for i in range(len(max({self.cardinal, inset.cardinal}))):
            if self.elements[i] in inset.elements[i]:
                outset.elements.append(self.elements[i])
        return outset
