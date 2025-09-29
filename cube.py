def cube(number):
    return number*number*number

num = int(input("Enter an integer: "))

# Check if number is divisible by 3 or not 

def y_3(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
    
print(f"The cube of {num} is: {cube(num)} ")
print("if number is divisible by 3 then returning its cube as",y_3(num))