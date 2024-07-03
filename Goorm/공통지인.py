N, M = map(int, input().split())

li1=[]
li2=[]

for i in range(N):
    li1.append(input())

for i in range(M):
    li2.append(input())

if set(li1).intersection(li2):
    for i in set(li1).intersection(li2):
        print(i)
else:
    print(-1)