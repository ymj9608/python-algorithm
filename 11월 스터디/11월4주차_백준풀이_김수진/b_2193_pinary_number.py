N = int(input())
pinary = [0] * 91
pinary[1] = 1
pinary[2] = 1
pinary[3] = 2

if N == 1 or N == 2:
    print(1)
elif N == 3:
    print(2)
else:
    for i in range(4, 91):
        pinary[i] = pinary[i-2] + pinary[i-1]
        if N == i:
            print(pinary[i])
            break

# def pinary_number(num):
#     if num == 1:
#         return 1
#     elif num == 2:
#         return 1
#     else:
#         return pinary_number(num-1) + pinary_number(num-2)
#
# N = int(input())
#
# print(pinary_number(N))