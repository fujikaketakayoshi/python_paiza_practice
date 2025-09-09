n = int(input())
a = int(input())
s = input().strip()
b = int(input())

trees = list(range(1, n + 1))  # 1..N
order = []

# 最初の木 A
idx = trees.index(a)
order.append(trees.pop(idx))

# 残りを順番に
while trees:
    if s == "CW":
        idx = (idx + b - 1) % len(trees)
    else:  # CCW
        idx = (idx - (b - 1)) % len(trees)

    order.append(trees.pop(idx))

print(" ".join(map(str, order)))
