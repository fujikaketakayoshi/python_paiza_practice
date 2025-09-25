h, w = map(int, input().split())
n = int(input())

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

score_map = {}
for _ in range(n):
    ty, tx, po, sp = map(int, input().split())
    score_map[(ty, tx)] = po
    for dir in range(8):
        ny, nx = ty + dy[dir], tx + dx[dir]
        if 1 <= ny <= h and 1 <= nx <= w:
            score_map[(ny, nx)] = sp

m = int(input())
score = 0
for _ in range(m):
    hy, hx = map(int, input().split())
    score += score_map.get((hy, hx), 0)

print(score)
