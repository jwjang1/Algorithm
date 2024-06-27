N = int(input())
direction = list(input().split())

location = [1,1]

for i in direction:
    if i == 'R' and location[1] != N:
        location[1] += 1

    if i == 'L' and location[1] != 1:
        location[1] -= 1

    if i == 'U' and location[0] != 1:
        location[0] -= 1
 
    if i == 'D' and location[0] != N:
        location[0] += 1

print(location[0], location[1]) 