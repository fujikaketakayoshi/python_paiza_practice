h, w = map(int, input().split())
grid = [[0] * w for _ in range(h)]
n = int(input())

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(n):
    ty, tx, po, sp = map(int, input().split())
    grid[ty - 1][tx - 1] = po
    for dir in range(8):
        ny = ty + dy[dir]
        nx = tx + dx[dir]
        if ny < 1 or nx < 1 or ny > h or nx > w:
            continue
        grid[ny - 1][nx - 1] = sp

m = int(input())
score = 0
for _ in range(m):
    hy, hx = map(int, input().split())
    score += grid[hy - 1][hx - 1]

print(score)
