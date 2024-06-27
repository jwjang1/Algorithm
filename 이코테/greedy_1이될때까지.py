# N, K = map(int, input().split())

# res = 0

# while N != 1:
#     if N % K == 0:
#         N /= K
#         res += 1
#     else:
#         N -= 1
#         res += 1

# print(res)

N, K = map(int,input().split())
cnt = 0

while N >= K:
    if N%K ==0:
        N//=K
        cnt+=1
    else:
        cnt+=N%K      
        N -= N%K
print(cnt)