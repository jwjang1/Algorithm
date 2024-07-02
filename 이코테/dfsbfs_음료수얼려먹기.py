N, M = map(int, input().split())

tray = []

for i in range(N):
    tray.append(list(map(int, input())))

icecream = 0


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if tray[x][y] == 0:
        tray[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True

    else:
        return False

for row in range(N):
    for col in range(M):
        if tray[row][col] == 0:
            res = dfs(row, col)
            if res == True:
                icecream += 1

print(icecream)