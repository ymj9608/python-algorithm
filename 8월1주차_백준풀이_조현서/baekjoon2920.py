# 8개의 숫자(음계)가 배열로 주어짐
arr = list(map(int, input().split()))

# 오름차순
if arr == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
# 내림차순      
elif arr == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
# 이 외     
else:
    print("mixed")