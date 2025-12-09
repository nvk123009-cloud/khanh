class oioi():
    def __init__(self):
        self.str =""

    def get(self):
        self.str = input()

    def print(self):
        print(self.str.upper())

str = oioi()
str.get()
str.print()