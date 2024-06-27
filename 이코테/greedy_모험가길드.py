N = int(input())
people = list(map(int, input().split()))

people.sort()

# num_guilds = 0

# while len(people) > people[0]:
#     if people[people[0]-1]<len(people):
#         del people[0:people[0]-1]
#         num_guilds += 1
#     else:
#         break

# print(num_guilds)


count = 0
num_guilds = 0
for i in people:
    count += 1
    if count >= i:
        num_guilds += 1
        count = 0