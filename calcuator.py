# Calcuator 

def addition(P, Q):
    return P + Q

def subtraction(P, Q):
    return P - Q

def multiplication(P, Q):
    return P * Q

def division(P, Q):
    return P / Q

print("Welcome to the Python Calcuator")
print("Please select one of the operations:")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

choice = input("Please enter your choice (a/b/c/d): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == 'a':
    print(num1, "+", num2, " = ", addition(num1, num2)) 
elif choice == 'b':
    print(num1, "-", num2, " = ", subtraction(num1, num2)) 
elif choice == 'c':
    print(num1, "*", num2, " = ", multiplication(num1, num2)) 
elif choice == 'd':
    print(num1, "/", num2, " = ", division(num1, num2)) 
else:
    print("This is an invalid input")