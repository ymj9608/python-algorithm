N = int(input())

if N % 5 == 0:
    result = N // 5
elif N // 5 == 0:
    if N % 3 == 0:
        result = 1
    else:
        result = -1
elif N // 5 == 1:
    if N % 3 == 0:
        result = N // 3
    elif N % 8 == 0:
        result = N // 8 * 2
    else:
        result = -1
else:
    if N % 5 == 1 or N % 5 == 3:
        result = N // 5 + 1
    else:
        result = N //5 + 2

print(result)