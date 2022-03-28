from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  should_continue = True
  num1 = float(input("What's the first number? "))
  for x in operations:
    print(x)
  while should_continue:
    symbol = input("Pick an operation from the options ")
    num2 = float(input("What's the next number? "))
    answer = operations[symbol](num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")
    next_act = input(f"Type 'y' to continue calculating with {answer} or 'n' to begin new calculation: ").lower()
    if next_act == 'y':
      num1 = answer
    elif next_act == 'n':
      calculator()
    else:
      should_continue = False

calculator()