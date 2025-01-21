N, X = map(int, input().split())
num = list(map(int, input().split()))

total = sum(num)
if total % X == 0:
    print(1)
else:
    print(0)