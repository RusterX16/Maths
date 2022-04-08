from Set import Set


class Graph:

    def __init__(self, *args):
        if len(args) == 1:
            pass

        if len(args) == 2:
            if isinstance(args[0], Set) and isinstance(args[1], Set):
                self.peaks = args[0]
                self.bones = args[1]
            if isinstance(args[0], list) and isinstance(args[0], list):
                self.bones = Set(args[1])
                self.peaks = Set(args[0])

    def tostring(self):
        return "G=(X=" + self.peaks.tostring() + ", E=" + self.bones.tostring() + ")"

    def display(self):
        print(self.tostring())

    def order(self):
        return self.peaks.cardinal

    def size(self):
        return self.bones.cardinal

    def is_complete(self):
        return self.order() * (self.order() - 1) / 2 == self.size()

    def complementary(self):
        bones = Set()

        for i in range(self.order()):
            for j in range(self.order()):
                a = (i + 1) * 10 + (j + 1)
                b = (j + 1) * 10 + (i + 1)
                contains_a = bones.contains(a)
                contains_b = bones.contains(b)

                if i == 0 or i == j or j == 0:
                    continue
                if not (contains_a or contains_b):
                    bones.add(a)
        return Graph(self.peaks, bones)
