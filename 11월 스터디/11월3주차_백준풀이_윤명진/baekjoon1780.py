import sys
input = sys.stdin.readline

def divide(divide_paper, size):
    global zero_papers, minus_one_papers, one_papers
    zero_cnt = minus_one_cnt = one_cnt = 0
    for row in divide_paper:
        zero_cnt += row.count(0)
        minus_one_cnt += row.count(-1)
        one_cnt += row.count(1)

    # 만약 모두 같은 것으로 채워졌다면 0 또는 1 또는 -1의 개수가 size ** 2이 될 것.
    if zero_cnt == size ** 2:
        zero_papers += 1

    elif minus_one_cnt == size ** 2:
        minus_one_papers += 1

    elif one_cnt == size ** 2:
        one_papers += 1

    # 아니면 9등분
    else:
        for i in range(0, size, size//3):
            for j in range(0, size, size//3):
                new_paper = []

                start_i = i
                end_i = i + size//3
                start_j = j
                end_j = j + size//3
                for row in range(start_i, end_i):
                    new_paper.append(divide_paper[row][start_j:end_j])

                divide(new_paper, size//3)

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

zero_papers = 0
minus_one_papers = 0
one_papers = 0

divide(paper, N)

print(minus_one_papers)
print(zero_papers)
print(one_papers)