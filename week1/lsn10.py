def combination(n, k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return combination(n - 1, k) + combination(n - 1, k - 1)


n, k = map(int, input().split())
print(combination(n, k))
