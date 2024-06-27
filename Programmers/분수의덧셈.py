numer1 = int(input())
denom1 = int(input())
numer2 = int(input())
denom2 = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return(gcd(b, a%b))
    
if denom1 != denom2:
    numer = (numer1*denom2 + numer2*denom1)
    denom = (denom1*denom2)
else:
    numer = numer1 + numer2
    denom = denom1

div = gcd(numer, denom)

print([int(numer/div), int(denom/div)])
