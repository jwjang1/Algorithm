def solution(food):
    res = ''
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            if food[i] != 1:
                res += str(i)
    
    rev = ''
    for i in res:
        rev = str(i) + rev
        
    res += '0'
    res += rev
    return(res)