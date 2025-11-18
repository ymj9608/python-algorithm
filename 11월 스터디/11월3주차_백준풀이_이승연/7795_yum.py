import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
  N, M = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  # 내림차순으로 정렬
  a.sort(reverse = True)
  b.sort(reverse = True)

  idx = 0
  result = 0

  # A가 기준
  for i in range(len(a)):
    # B의 원소의 개수만큼만 비교
    while idx < len(b):
      if a[i] > b[idx]:
        # 비교하는 B의 원소가 A의 원소보다 작으면
        # B의 해당 원소보다 작은 것들은 (개수가 idx개) 더이상 카운트안하고 break
        result += (len(b) - idx)
        break
      
      # 그게 아니면 그다음꺼 비교
      else:
        idx += 1

  print(result)