# 알바생 강호
import sys
input = sys.stdin.readline

N = int(input())
tips = [int(input()) for _ in range(N)]

# 내림차순 정렬
tips.sort(reverse=True)

result = 0
for idx, tip in enumerate(tips):
    # idx는 인덱스이므로 -1 할 필요 없음
    real_tip = tip - idx

    # 실제 팁이 음수나 0이 되면 
    # 그 전까지가 최댓값이므로 즉시 break
    if real_tip <= 0:
        break
    result += real_tip

print(result)