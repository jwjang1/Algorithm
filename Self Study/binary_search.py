def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end)//2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
len, target = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = len - 1
print(binary_search(arr, target, start, end))