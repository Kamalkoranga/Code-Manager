def calculate():
  num1 = int(input('Enter 1st number: '))
  operator = input('Enter any operator: ')
  num2 = int(input('Enter 2nd number: '))
  if operator == '+':
      print(num1 + num2)
  elif operator == '-':
      print(num1 - num2)
  elif operator == '*':
      print(num1 * num2)
  elif operator == '/':
      print(num1 / num2)
