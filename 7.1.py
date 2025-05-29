lst = input("Enter elements: ").split()
rot_num = int(input("Enter rotation number: "))
split_num = rot_num % len(lst)
rotated_lst = lst[split_num:] + lst[:split_num]
print("Rotated List:", rotated_lst)
