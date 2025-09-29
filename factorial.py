def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        # Recursive Function Calling
        return x * factorial(x-1)

num = int(input("Enter your number: "))

if num < 0:
    print("There isn't a factorial for negative numbers!")
else: 
    print(f"The factorial of {num} is {factorial(num)}")