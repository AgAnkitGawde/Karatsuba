def karat(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        n2 = n // 2
        a = x // 10**(n2)
        b = x % 10**(n2)
        c = y // 10**(n2)
        d = y % 10**(n2)

        z0 = karat(b,d)
        z1 = karat((a+b),(c+d))
        z2 = karat(a,c)

        return (z2 * 10**(2*n2)) + ((z1 - z2 - z0) * 10**(n2)) + (z0)

x,y=input().split()
x=int(x)
y=int(y)
print(karat(x,y))
