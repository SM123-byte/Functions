def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end =' ')

num1 = int(input("Enter an integer: "))

DecimalToBinary(num1)