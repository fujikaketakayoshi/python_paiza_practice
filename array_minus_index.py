arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = 4
step = 3
dir = "CCW"
while arr:
    if dir == "CW":
        idx = (idx + step) % len(arr)
    else:
        idx = (idx - step) % len(arr)
    print(arr.pop(idx))
