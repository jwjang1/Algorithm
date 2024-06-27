m = int(input())
score = list(map(int, input().split()))

score = sorted(score, reverse=True)
res = 0

for i in range(0, len(score), m):
    if len(score[i:i+m]) == m:
        res += min(score[i:i+m]) * m

print(res)