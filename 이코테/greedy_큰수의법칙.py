N, M, K = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
final = 0
first = num[-1]
second = num[-2]
count = 0

for i in range(M):
    if count == K:
        final += second
        count = 0
    else:
        final += first
        count += 1

print(final)