import sys
input = sys.stdin.readline

N = int(input())

first_str = input().rstrip()
# A~Z 카운팅 배열
first_alpha = [0] * 26

for x in first_str:
    first_alpha[ord(x) - ord('A')] += 1

# 비슷한 단어의 개수 체크
similar_count = 0
for _ in range(N - 1):
    string = input().rstrip()
    second_alpha = [0] * 26

    for x in string:
        second_alpha[ord(x) - ord('A')] += 1

    diff_count = 0
    # 다른 문자의 개수 카운팅
    for i in range(26):
        diff_count += abs(first_alpha[i] - second_alpha[i])

    # 길이가 같으면
    if len(first_str) == len(string):
        # 예를 들어
        # DOG, GOD의 경우: diff_count = 0
        # DOG, DIG의 경우 diff_count = 2
        # 즉, diff_count는 0 또는 2이어야 함.
        if diff_count == 0 or diff_count == 2:
            similar_count += 1

    # 길이가 다르면
    else:
        # 예를 들어
        # DOGL, DOG의 경우: diff_count = 1
        if diff_count == 1:
            similar_count += 1

print(similar_count)