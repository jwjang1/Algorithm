pos = input()

li = list('abcdefgh')
count = 0

row = li.index(pos[0])
col = int(pos[1])-1

dir = [(-1,-2), (-1,2), (1,-2), (1,2), (-2,-1), (-2,1), (2,-1), (2,1)]

for i in range(len(dir)):
    if row + dir[i][0] >= 0 and row + dir[i][0] <= 7 and col + dir[i][1] >= 0 and col + dir[i][1] <= 7:
        count += 1


print(count)