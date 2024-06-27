N = int(input())

five_hundred = 0
one_hundred = 0
fifty = 0
ten = 0

while(N >= 500):
    N -= 500
    five_hundred += 1

while(N >= 100):
    N -= 100
    one_hundred += 1

while(N >= 50):
    N -= 50
    fifty += 1

while(N >= 10):
    N -= 10
    ten += 1

res = five_hundred + one_hundred + fifty + ten
print(res)