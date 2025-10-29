N, M = map(int, input().split())

Pokemon_dict = []
for i in range(N):
    pokemon = input().strip()
    Pokemon_dict.append(pokemon)

for j in range(M):
    check = input().strip()
    if check.isdigit():
        print(Pokemon_dict[int(check) - 1])
    else:
        print(Pokemon_dict.index(check) + 1)