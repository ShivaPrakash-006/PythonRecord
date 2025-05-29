def gcd(a, b):
    if a > b:
        x, y = a, b
    else:
        x, y = b, a

    if y == 0:
        return x
    else:
        return gcd(x % y, y)


num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))
