x = 451

coins = [500, 100, 50, 10, 5, 1]
total = 0
for i in coins:
    num = x // i
    total += num
    x -= i * num

print(total)
