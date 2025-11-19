import sys

input = sys.stdin.readline

def find_min_diff(idx, total_sour, total_bitter):
    global min_diff
    # 모든 재료를 넣을지 말지 결정했다면, 최종 맛의 차이 계산 후 비교하여 min_diff 갱신
    if idx == N:
        # 이때 쓴맛은 양의 정수이므로 total_bitter이 0이라는 것은 모든 재료가 들어가지 않은 경우임
        # 즉, 최솟값 갱신하지 않기
        if total_bitter == 0:
            return
        else:
            total_diff = abs(total_sour - total_bitter)
            min_diff = min(min_diff, total_diff)
            return
    

    # idx번째 재료 포함 X
    find_min_diff(idx + 1, total_sour, total_bitter)
    # idx번째 재료 포함 O (신맛 = 누적 신맛 * idx번째 재료의 신맛, 쓴맛 = 누적 쓴맛 + idx번째 재료의 쓴맛)
    find_min_diff(idx + 1, total_sour * ingredients[idx][0], total_bitter + ingredients[idx][1])


N = int(input())

ingredients = [list(map(int, input().split())) for _ in range(N)]
min_diff = float('inf')


find_min_diff(0, 1, 0)
print(min_diff)