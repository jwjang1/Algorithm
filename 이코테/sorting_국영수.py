n = int(input())
li = []

for i in range(n):
    stu = input().split()
    li.append((stu[0], int(stu[1]), int(stu[2]), int(stu[3])))

li = sorted(li, key= lambda x:(-x[1], x[2], -x[3], x[0][0].lower(), x[0][1:]))

for i in range(n):
    print(li[i][0])