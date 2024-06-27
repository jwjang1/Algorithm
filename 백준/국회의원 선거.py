N = int(input())
votes = []
mine = int(input())

for i in range(N-1):
    votes.append(int(input()))

count = 0

if N == 1:
        print(0)
else:
    while mine <= votes[votes.index(max(votes))]:
        votes[votes.index(max(votes))] -= 1
        mine += 1
        count += 1
    print(count)