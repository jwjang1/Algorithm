n = int(input())
li = []

for i in range(n):
    li.append(int(input()))

li = sorted(li, reverse=True)

for i in li:
    print(i, end=' ')