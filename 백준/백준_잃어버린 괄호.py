equation =input().split('-')

split_eq = []
for i in range(len(equation)):
    split_eq.append(equation[i].split('+'))

res = 0
for i in range(len(split_eq)):
    for j in range(len(split_eq[i])):
        if i == 0:
            res += int(split_eq[i][j])
        else:
            res -= int(split_eq[i][j])

print(res)+6