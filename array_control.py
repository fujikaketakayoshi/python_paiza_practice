lst = [1, 2, 3, 4]
for i in lst:
    i *= 2
print(lst)


lst3 = [x * 2 for x in lst]
print(lst3)  # [2, 4, 6, 8]