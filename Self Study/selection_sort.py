li = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(li)):
    idx = i

    for j in range(i+1, len(li)):
        if li[j] < li[idx]:
            idx = j
        
    li[i], li[idx] = li[idx], li[i]

print(li)