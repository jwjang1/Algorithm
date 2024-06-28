def solution(nums):
    n = len(nums)//2
    unique = set(nums)
    pokemon_li = list(unique)
    if n > len(pokemon_li):
        print(len(pokemon_li))
    else:
        print(n)