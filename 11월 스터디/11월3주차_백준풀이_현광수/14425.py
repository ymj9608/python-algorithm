N, M = map(int, input().split())

word_list = set()
cnt = 0

for _ in range(N):
    word = input()
    word_list.add(word)

for _ in range(M):
    check = input()
    if check in word_list:
        cnt += 1

print(cnt)