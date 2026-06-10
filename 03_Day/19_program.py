for i in range(1, 1001):
    total = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            total += j
    if total == i:
        print(i)