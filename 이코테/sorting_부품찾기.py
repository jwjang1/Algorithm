N = int(input())
li = list(map(int, input().split()))
M = int(input())
req = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end)//2

    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in range(M):
    if binary_search(li, req[i], 0, N-1) != None:
        print('yes', end=' ')
    else:
        print('no', end= ' ')
