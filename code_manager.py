'''
* CODE MANAGER
'''


from inspect import getsource
from packages.GTN import gtn
from packages.calculator import calculate
import shutil
from packages import *


class Code():
    def __init__(self, language, i=0, fn='', code=''):
        self.language = language
        self.i = i
        self.fn = fn
        self.code = code

        while self.i == 0:
            self.main()

    def main(self):
        print(f">>>>>>>>> CODE MANAGER({self.language}) <<<<<<<<<<")
        print("Features:-")
        print(" 1 - Add Code")
        print(" 2 - Run Codes")
        print(" 3 - Show Codes")
        print(" 4 - Exit")

        choose = int(input("Choose any feature: "))
        if choose == 1:
            self.add()
        elif choose == 2:
            self.run()
        elif choose == 3:
            self.show()
        elif choose == 4:
            self.i = 1

    def add(self):
        self.fn = input("Enter file name: ")
        file = open(self.fn, 'x', )
        # =========== Multi-line input here!!
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line +'\n')
            else:
                break
            self.code = '\n'.join(lines)
        file.writelines(lines) # adds lines variable in file
        file = open(self.fn) # open the file
        # print(self.code) # prints the code
        file.close()

        shutil.move(f"./{self.fn}", f"./packages/{self.fn}")
        
    def run(self):
        which = int(input("Which code you want to run: "))
        if which == 1:
            print(" ======== Calculator =============")
            calculate()
        
        elif which == 2:
            print(" ======== Gues The Number =============")
            gtn()
        
        elif which == 3:
            print(f" ======== {self.fn} =============")
            exec(open(f'packages/{self.fn}').read()) # executes another py file

        elif which == 4:
            print(f" ======== {self.fn} =============")
            exec(open(f'packages/{self.fn}').read())

    def show(self):
        which = int(input("which: "))
        if which == 1:
            print(" ======== Calculator =============")
            print(getsource(calculate))
        
        elif which == 2:
            print(" ======== Calculator =============")
            print(getsource(gtn))
        
        elif which == 3:
            # print(f" ======== {self.fn.strip('.py')} =============") # strip function allow us to remove character
            print(f" ======== {self.fn} =============")
            print(self.code)

        elif which == 3:
            print(f" ======== {self.fn} =============")
            print(self.code)


fir = Code('py')
# fir.add()