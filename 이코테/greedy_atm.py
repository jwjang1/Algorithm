N = int(input())
times = list(map(int, input().split()))

sorted_times =sorted(times)
total = 0

for i in range(1, N+1):
    total += sum(sorted_times[0:i])

print(total)