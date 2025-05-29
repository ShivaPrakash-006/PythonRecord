num = int(input("Enter Upper Limit: "))

squares = {x: x**2 for x in range(1, num + 1) if x % 2 == 0}
print("Even number squares:", squares)
