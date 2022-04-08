# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Function import Function
from Graph import Graph
from Set import Set


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    s = Set([1, 2, 4, 5])

    print("2 in set ? " + str(s.contains(2)))
    print("3 in set ? " + str(s.contains(3)))

    g = Graph([1, 2, 3, 4], [12, 13, 14])
    g2 = Graph([1, 2, 3], [12, 23, 31])
    g.display()                 # G=(X={1, 2, 3, 4, 5} E={12, 13, 14, 23})

    print(g.order())            # 5
    print(g.size())             # 4

    print(g.is_complete())      # False
    print(g2.is_complete())     # True

    g.complementary().display()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
