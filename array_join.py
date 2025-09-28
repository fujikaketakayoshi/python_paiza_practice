lst = ['a', 'b', 'c', 'd']
print('-'.join(lst))  # a-b-c-d
print(''.join(lst))   # abcd
print(', '.join(lst)) # a, b, c, d

arr = [1, 2, 3, 4 / 5]
print(" ".join(map(str, arr)))
