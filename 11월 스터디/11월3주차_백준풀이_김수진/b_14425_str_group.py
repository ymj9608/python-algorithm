N, M = map(int, input().split())
S = [input() for _ in range(N)]
checks = [input() for _ in range(M)]

result = 0

# S를 세트로 변환하여 추가했을 때 길이가 변하는지 체크하여 같은 것을 확인
for check in checks:
    s = set(S)
    s.add(check)
    if len(s) == N:
        result += 1

print(result)

# S = [input().strip() for _ in range(N)]
#
# result = 0
# for _ in range(M):
#     check = input()
#     if check in S:
#         result += 1
#
# print(result)

# for m_str in M:
#     for s_str in S:
#         if m_str == s_str:
#             result += 1



# # 검사해야 하는 문자열 하나씩 검사
# for m_str in M:
#     ml = len(m_str)
#     # 집합 S에 있는 문자열들과 대조
#     for s_str in S:
#         sl = len(s_str)
#         if ml > sl:
#             pass
#         elif ml == sl:
#             if m_str == s_str:
#                 result += 1
#                 continue
#         else:
#             find = False
#             # s_str 순회하면서 m_str의 첫 번째와 일치하는지 체크
#             for i in range(sl):
#                 # 첫 번째와 일치하고, 길이가 가능할 것 같으면
#                 if s_str[i] == m_str[0] and sl - i >= ml:
#                     # 슬라이싱 해서 대조
#                     if m_str == s_str[i:i+ml]:
#                         result += 1
#                         find = True
#                         break


