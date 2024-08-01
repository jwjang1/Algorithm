n, k = map(int, input().split())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

li_a = sorted(li_a)
li_b = sorted(li_b, reverse=True)

for i in range(k):
    if li_a[i] < li_b[i]:
        li_a[i] = li_b[i]
    
    else:
        break

print(sum(li_a))