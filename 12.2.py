def root(x):
    if x < 0:
        raise ValueError("No Negative Numbers")
    else:
        return x**0.5


try:
    num = int(input("Enter number: "))
    print(root(num))
except ValueError as err:
    print("Invalid Input:", err)
except Exception as err:
    print("Unexpected Error:", err)
