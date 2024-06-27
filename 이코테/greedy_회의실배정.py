N = int(input())
sched=[]

# for i in range(N):
#     sched.append(list(map(int, input().split())))
sched = [list(map(int, input().split())) for i in range (N)]

sched.sort(key = lambda x:(x[1], x[0]))

count = 1
cur = sched[0][1]

for i in range(1, len(sched)):
    if sched[i][0] >= cur:
        cur = sched[i][1]
        count += 1

print(count)