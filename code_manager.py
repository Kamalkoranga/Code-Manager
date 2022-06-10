'''
* CODE MANAGER
'''


from inspect import getsource
from GTN import gtn
from calculator import calculate
from . import *


class Code():
    def __init__(self, language, i=0):
        self.language = language
        self.i = i

        # while self.i == 0:
        #     self.main()

    def main(self):
        print(f">>>>>>>>> CODE MANAGER({self.language}) <<<<<<<<<<")
        print("Features:-")
        print(" 1 - Show Codes")
        print(" 2 - Run Codes")
        print(" 3 - Exit")

        choose = int(input("Choose any feature: "))
        if choose == 1:
            self.show()
        elif choose == 2:
            self.run()
        elif choose == 3:
            self.i = 1
        
    def run(self):
        which = int(input("Which code you want to run: "))
        if which == 1:
            print(" ======== Calculator =============")
            calculate()
        
        elif which == 2:
            print(" ======== Gues The Number =============")
            gtn()

    def show(self):
        which = int(input("which: "))
        if which == 1:
            print(" ======== Calculator =============")
            print(getsource(calculate))
        
        elif which == 2:
            print(" ======== Calculator =============")
            print(getsource(gtn))
        
        elif which == 3:
            print(getsource())

    def add(self):
        fn = input("Enter file name: ")
        file = open(fn, 'x')
        # =========== Multi-line input here!!
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        code = '\n'.join(lines) # add all inputs in a list

        file.writelines(lines) # adds lines variable in file
        file = open(fn) # open the file
        print(code) # prints the code


fir = Code('Python')
fir.add()