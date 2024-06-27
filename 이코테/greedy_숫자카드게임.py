N, M = map(int, input().split())

cardlist=[]

for i in range(N):
    cardlist.append(list(map(int, input().split())))

min_num = []
for i in range(N):
    min_num.append(min(cardlist[i]))

res = 0
res = max(min_num)
print(res)