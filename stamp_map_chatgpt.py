h, w, n = map(int, input().split())

# スタンプの読み込み
tiles = []
for _ in range(n):
    tile = [input() for _ in range(h)]
    tiles.append(tile)

r, c = map(int, input().split())
layout = [list(map(int, input().split())) for _ in range(r)]

# 結果を構築
for i in range(r):
    # 各スタンプ行ごとに処理
    for row in range(h):
        line = ""
        for j in range(c):
            line += tiles[layout[i][j] - 1][row]
        print(line)
