try:
    divident = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    print(divident / divisor)
except ZeroDivisionError:
    print("Cannot divide by zero")
