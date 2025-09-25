import random

H, W = 100, 100
N = 100
M = 1000

print(H, W)
print(N)

# 的の配置（10マス間隔で安全に置く）
for i in range(1, N + 1):
    r = (i % 10) * 10 + 1
    c = (i // 10) * 10 + 1
    p = 100
    q = 50
    print(r, c, p, q)

print(M)

# 射撃座標（ランダムに 1000 発）
for _ in range(M):
    a = random.randint(1, H)
    b = random.randint(1, W)
    print(a, b)
