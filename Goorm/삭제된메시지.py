N, M = map(int, input().split())
li = []
for i in range(M):
    li.append(input().split())


for i in range(M):
    if (li[i][1]).isdigit():
        count = 1
        for j in range(i):
            if (int(li[j][0]) == int(li[i][0])) and ((str(li[j][1]).isalpha())) and (int(li[i][1]) == count):
                li[j][1] = -1
                break
            elif(int(li[j][0]) == int(li[i][0])):
                count += 1


res = [x for x in li if x[1] != -1 and x[1].isalpha()]
print(res)