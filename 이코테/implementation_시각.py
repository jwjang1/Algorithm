n = int(input())

count = 0

for i in range(n+1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(i) + str(min) + str(sec):
                count += 1

print(count)