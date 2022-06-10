'''
* CODE MANAGER
'''


from inspect import getsource
from GTN import gtn
# from calculator import calculate


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
            # calculate()
        
        elif which == 2:
            print(" ======== Gues The Number =============")
            gtn()

    def show(self):
        which = int(input("which: "))
        if which == 1:
            print(" ======== Calculator =============")
            # print(getsource(calculate))
        
        elif which == 2:
            print(" ======== Calculator =============")
            print(getsource(gtn))

    def add(self):
        # file = open("calculator.py", "w")
        # file.write("print('Hello World!')")
        # file = open("GTN.py")
        # file = open("calculator.py")
        # content = file.read()
        # file.close()
        # print(content)

        # print(file)

        file = open("demo.py", 'w')
        lines = ["def calculate():\n", 
                 "  num1 = int(input('Enter 1st number: '))\n",
                 "  operator = input('Enter any operator: ')\n",
                 "  num2 = int(input('Enter 2nd number: '))\n",

                 "  if operator == '+':\n",
                 "      print(num1 + num2)\n",
                 "  elif operator == '-':\n",
                 "      print(num1 - num2)\n",
                 "  elif operator == '*':\n",
                 "      print(num1 * num2)\n",
                 "  elif operator == '/':\n",
                 "      print(num1 / num2)\n"
                ]
        file.writelines(lines)
        file = open("demo.py")
        content = file.read()
        # print(content)

        fil1 = open("GTN.py")
        print(fil1.read())


fir = Code('Python')
fir.add()