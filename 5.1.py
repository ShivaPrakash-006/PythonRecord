def sum(num):
    if num <= 1:
        return num
    return num + sum(num - 1)


nat_nums = int(input("Enter number: "))
print("Sum of first", nat_nums, "natural numbers is", sum(nat_nums))
