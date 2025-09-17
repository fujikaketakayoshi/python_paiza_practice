n, m = map(int, input().split())
wins = [tuple(map(int, input().split())) for _ in range(m)]

# 各園児の親（列車の代表を指す）
parent = list(range(n + 1))
# 各列車の長さ（代表ノードにだけ有効）
size = [1] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for x, y in wins:
    # それぞれ列車の先頭（代表）を取得
    rx, ry = find(x), find(y)
    # x が勝ったので、y の列車を x 側にくっつける
    parent[ry] = rx
    size[rx] += size[ry]
    size[ry] = 0  # もう使わない

# 最大の長さを求める
max_len = max(size)

# 長さが最大の列車の「先頭園児」を出力
ans = []
for i in range(1, n + 1):
    if parent[i] == i and size[i] == max_len:
        ans.append(i)

for a in sorted(ans):
    print(a)
