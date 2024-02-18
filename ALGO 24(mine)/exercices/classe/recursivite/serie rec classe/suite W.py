def W(n):
    if n == 0:
        return 1
    else:
        return W(n-1) + 2*(n)
n = int(input('donner n : '))
print(W(n))
