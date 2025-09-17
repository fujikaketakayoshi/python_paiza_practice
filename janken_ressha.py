n, m = map(int, input().split())

wins = [list(map(int, input().split())) for _ in range(m)]

train = {}
for i in range(1, n + 1):
    train[i] = [i]

for win in wins:
    train[win[0]].extend(train[win[1]])
    del train[win[1]]

result = []
max_num = 0
for num, arr in train.items():
    num_vol = len(arr)
    if max_num < num_vol:
        result = [num]
        max_num = num_vol
    elif max_num == num_vol:
        result.append(num)

for i in result:
    print(i)
