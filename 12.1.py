try:
    divident = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    print(divident / divisor)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception as err:
    print("Unexpected Error:", err)
