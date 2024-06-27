s = input()


half = int(len(s)/2+1)
compare = []
for i in range(1, half):
    count = 0
    divided=''
    for k in range(0, len(s), i):
        if s[k:k+i] == s[k+i:k+2*i]:
            count += 1
        elif count >= 1:
            divided += str(count+1)
            divided += s[k:k+i]
            count = 0
        else:
            divided += s[k:k+i]
            
    compare.append(len(divided))

print(min(compare))

