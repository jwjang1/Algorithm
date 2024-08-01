li = [1,5,2,7,9,3]

for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[j] < li[i]:
            li[i], li[j] = li[j], li[i]

print(li)