num = int(input("Enter number of rows: ")) + 1
for i in range(num):
    for j in range(num - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        if (k == 0 or k == 2 * i - 2) or i == num - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
