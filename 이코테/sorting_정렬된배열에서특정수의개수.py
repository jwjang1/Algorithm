N, x = map(int, input().split())
li = list(map(int, input().split()))

def binary_search_left(array, target, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        if mid > 0 and array[mid-1] == target:
            return binary_search_left(array, target, 0, mid-1)
        else:
            return mid
    elif array[mid] > target:
        return binary_search_left(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search_left(array, target, mid+1, end)
    

def binary_search_right(array, target, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        if array[mid+1] == target:
            return binary_search_right(array, target, mid+1, end)
        else:
            return mid
    elif array[mid] > target:
        return binary_search_right(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search_right(array, target, mid+1, end)
    
start = 0
end = N-1
left = binary_search_left(li, x, start, end)
right = binary_search_right(li, x, start, end)

if left != None and right != None and (right - left) >= 0:
    print(right - left + 1)
else:
    print(-1)