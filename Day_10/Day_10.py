import art

print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "x" or "*": multiply,
    "/": divide
}

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

for symbol in operations:
    print(symbol)
operationChoice = input("What would you like to do? ")

calculation_function = operations[operationChoice]
result = calculation_function(n1, n2)

print(f"{n1} {operationChoice} {n2} = {result}")

n3 = result

continueOption = input(f"Would you like to continue with {result}? y/n \n")

while continueOption == 'y':
    n4 = int(input('Enter the next number: '))

    for symbol in operations:
        print(symbol)
    operationChoice = input("What operation would you like to perform? ")

    calculation_function = operations[operationChoice]

    new_result = calculation_function(n3, n4)

    print(f"{n3} {operationChoice} {n4} = {new_result}")

    n3 = new_result

    continueOption = input(f"Would you like to continue with {n3}? y/n \n")

print("Thank you for playing")