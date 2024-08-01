n = int(input())
li = []

for i in range(n):
    stu = input().split()
    li.append((stu[0], int(stu[1])))

li = sorted(li, key= lambda x:x[1])

for i in li:
    print(i[0], end=' ')