n = int(input())

win_num = 0
for i in range(n):
    line = input()
    a, b = line.split()
    if (a == 'G' and b == 'C') or (a == 'C' and b == 'P') or (a == 'P' and b == 'G'):
        win_num += 1

print(win_num)
