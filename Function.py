class Function:

    def __init__(self, letter, variable):
        self.letter = letter
        self.variable = variable

    def display(self):
        print(self.letter + "(" + self.variable + ")")