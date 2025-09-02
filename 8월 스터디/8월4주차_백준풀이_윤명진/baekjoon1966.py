T = int(input())

for _ in range(T):

    N, M = map(int, input().split())
    paper_list = list(map(int, input().split()))

    # 문서의 번호와 문서의 중요도를 묶어서 papers에 저장
    papers = [[i, paper_list[i]] for i in range(N)]

    # 출력한 횟수를 저장할 count 변수 생성
    count = 0
    while True:
        # 남은 문서의 수
        n = len(papers)

        # 가장 중요한 문서의 중요도 저장
        max_imp = papers[0][1]
        for i in range(n):
            if max_imp < papers[i][1]:
                max_imp = papers[i][1]

        # 가장 앞에 있는 문서의 중요도가 가장 중요한 문서보다 낮으면 뒤로 이동
        if papers[0][1] < max_imp:
            papers.append(papers.pop(0))

        # 가장 앞에 있는 문서의 중요도가 높고, 그것이 처음 지정한 M번째 종이가 아니면 출력(pop)시킨 후, count에 +1
        elif papers[0][1] >= max_imp and papers[0][0] != M:
            count += 1
            papers.pop(0)

        # 가장 앞에 있는 문서의 중요도가 높고, 그것이 처음 지정한 M번째 종이이면 count에 +1 한 다음, 반복문 종료
        elif papers[0][1] >= max_imp and papers[0][0] == M:
            count += 1
            break

    # 출력 횟수 출력
    print(count)