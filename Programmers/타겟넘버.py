numbers = list(map(int, input().split()))
target = int(input())
index = 0
sum = 0

def dfs (numbers, target, index):
    global sum
    if index+1 == len(numbers):
        if target + numbers[index] == 0:
            sum += 1
        elif target - numbers[index] == 0:
            sum += 1
        return
    dfs(numbers, target + numbers[index], index+1)
    dfs(numbers, target - numbers[index], index+1)

dfs(numbers, target, index)

print(sum)