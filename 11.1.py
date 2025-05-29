try:
    divident = int(input("Enter divident: "))
    divisor = int(input("Enter divisor: "))
    print(divident / divisor)
except ZeroDivisionError:
    print("Cannot divide by zero")
