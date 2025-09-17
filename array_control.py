lst = [1, 2, 3, 4]

lst2 = [x * 2 for x in lst]
print(lst2)

for i in range(len(lst)):
    lst[i] *= 2
print(lst)
