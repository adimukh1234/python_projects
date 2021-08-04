# selecting the type of operation
# add
def add(x, y):
    return x + y


# subtract
def subtract(x, y):
    return x - y


# division
def divide(x, y):
    return x / y


# multiplication
def multiply(x, y):
    return x * y


# list of operations
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter operation \n 1,2,3,4:\n"))
num1 = int(input("Enter First number\n"))
num2 = int(input("Enter Second number\n"))

# solving the problem
if choice == 1:
    ans = add(num1, num2)
    print(f"The answer is {ans}")
elif choice == 2:
    ans = subtract(num1, num2)
    print(f"The answer is {ans}")
elif choice == 3:
    ans = multiply(num1, num2)
    print(f"The answer is {ans}")
elif choice == 4:
    ans = divide(num1, num2)
    print(f"The answer is {ans}")

# thank you
print("Thanks for using this calculator")
