chars = ['d', 'a', 'b', 'c']
visited = [False] * len(chars)
result = []
def dfs(path):
    if len(path) == len(chars):
        result.append(''.join(path))
        return
    for i in range(len(chars)):
        if not visited[i]:
            visited[i] = True
            path.append(chars[i])
            dfs(path)
            path.pop()
            visited[i] = False

dfs([])
result.sort()
print('\n'.join(result))
