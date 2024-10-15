N, K = map(int, input().split())
li = {}
lim = K * 60

for i in range(N):
    cur = input().split()
    if cur[0] in li:
        li[cur[0]].append(cur[1])
    else:
        li[cur[0]] = [cur[1]]


time = {}
for i in li:
    time[i] = 0
    for j in range(len(li[i])):
        if j % 2 == 0:
            time[i] -= (int(li[i][j][0:2]) * 60 + int(li[i][j][3:]))
        else:
            time[i] += (int(li[i][j][0:2]) * 60 + int(li[i][j][3:]))


sum = 0
for i in time:
    if time[i] >= lim:
        sum += 1

print(sum)