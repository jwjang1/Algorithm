N, K = map(int, input().split())

floor = []
for i in range(N):
    floor.append(list(map(int, input().split())))

step = {}
steps = 0
for i in range(N):
    for j in range(N):
        if floor[i][j] != 0:
            step[floor[i][j]] = [i, j]

for i in range(2, K + 1):
    steps += abs(step[i-1][0] - step[i][0]) + abs(step[i-1][1] - step[i][1])

print(steps)