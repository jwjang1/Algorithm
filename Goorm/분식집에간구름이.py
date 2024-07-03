price1, price2, price3 = map(int, input().split())
dc1, dc2, dc3 = map(int, input().split())
num1, num2, num3 = map(int, input().split())

sum0 = price1 * num1 + price2 * num2 + price3 * num3

def dfs(num1, num2, num3, sum):
    global sum0

    if num1 < 0 or num2 < 0 or num3 < 0:
        return
    
    elif (num1 == 0 and num2 == 0) or (num1 == 0 and num3 == 0) or (num2 == 0 and num3 == 0):
        sum0 = min(sum0, sum)
         
    else:
        dfs(num1-1, num2-1, num3, sum-dc1)
        dfs(num1-1, num2, num3-1, sum-dc2)
        dfs(num1, num2-1, num3-1, sum-dc3)


dfs(num1, num2, num3, (price1 * num1 + price2 * num2 + price3 * num3))

print(sum0)