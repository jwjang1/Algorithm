N = int(input())
li = list(map(int, input().split()))

def binary_search(array, start, end):
    if start > end:
        return -1
    
    mid = (start + end)//2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)
    
start = 0
end = N-1
res = binary_search(li, start, end)
print(res)