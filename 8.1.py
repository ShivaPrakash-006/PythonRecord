tpl = (4, 9, 1, 7, 3, 6, 5, 2)
num = int(input("Enter number of results: "))

sorted_lst = sorted(tpl)
values = []
for i in range(num):
    values.append(sorted_lst[i])
for i in range((len(sorted_lst) - num), len(sorted_lst)):
    values.append(sorted_lst[i])

print("Min Values:", values[:num])
print("Max values:", values[num:])
