h, w, n = map(int, input().split())

tiles = []
for i in range(n):
    tile = [[] for _ in range(h)]
    for j in range(h):
        tile[j] = input()
    tiles.append(tile)

r, c= map(int, input().split())
rcs = []
for i in range(r):
    rcs.append(list(map(int, input().split())))

result = [[] for _ in range(h * r)]

for i, rs in enumerate(rcs):
    for j, col in enumerate(rs):
        for k, str in enumerate(tiles[col - 1]):
            result[i * h + k] += str

for i in result:
    print(''.join(i))
