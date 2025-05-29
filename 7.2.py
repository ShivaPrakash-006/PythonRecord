lst = input("Enter elements: ").split()
filtered_lst = [ele for ele in lst if "a" not in ele]
print("Filtered List:", filtered_lst)
