'''
問題文

N個の作業があり、
いくつかの作業には「先に終わらせるべき別の作業」があります。
作業の依存関係は M 本の有向辺 (a → b) で与えられます。

この依存関係をすべて満たすような作業順序を1つ出力してください。
もし不可能（閉路がある）なら -1 を出力してください。
'''

from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
indeg = [0] * N  # 入次数

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    indeg[b] += 1

# 入次数0のノードをキューに入れる
q = deque([i for i in range(N) if indeg[i] == 0])
ans = []

while q:
    v = q.popleft()
    ans.append(v + 1)  # 出力用に+1戻す
    for nxt in G[v]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            q.append(nxt)

# すべてのノードを処理できなかった場合 → 閉路あり
if len(ans) != N:
    print(-1)
else:
    print(*ans)
