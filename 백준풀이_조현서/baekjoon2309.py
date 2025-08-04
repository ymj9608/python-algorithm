list1 = [int(input()) for _ in range(9)]  # 일곱 난쟁이의 리스트를 설정

total = sum(list1)

for i in range(9):
    for j in range(i+1, 9):
        if total - (list1[i] + list1[j]) == 100:
            false1, false2 = list1[i], list1[j]

            result = [l for l in list1 if l != list1[i] and l != list1[j]]

            for r in sorted(result):
                print(r)

