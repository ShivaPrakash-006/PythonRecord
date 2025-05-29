set1 = set(input("Enter students in class 1: ").split())
set2 = set(input("Enter students in class 2: ").split())

commonSet = set1.intersection(set2)
print("Students in both classes:", commonSet)
