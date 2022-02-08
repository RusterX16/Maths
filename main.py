# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Function import Function
from Set import Set


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = Set()
    s.fill([1, 2, 3, 5])
    s.fill([5, 8, 9, 12])
    s.display()

    s2 = Set([1, 2, 6, 8])
    s = s.minus(s2)
    s.display()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
