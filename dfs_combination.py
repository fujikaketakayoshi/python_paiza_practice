chars = ['d', 'a', 'b', 'c']
chars.sort()  # ソートしておくと辞書順になる
result = []

def dfs(start, path, k):
    if len(path) == k:        # 長さkになったら出力
        result.append(''.join(path))
        return
    for i in range(start, len(chars)):
        path.append(chars[i])
        dfs(i+1, path, k)     # i+1から先を探索することで「順番無視」が実現
        path.pop()

k = 3  # 選ぶ長さ
dfs(0, [], k)

print('\n'.join(result))
