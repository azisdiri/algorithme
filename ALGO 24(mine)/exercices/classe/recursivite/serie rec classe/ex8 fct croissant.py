def cr(n):
    if (n < 10):
        return True
    else:
        return (n % 10) >= (n//10) % 10 and (cr(n//10))


# pp
n = int(input("donner n : "))
print(cr(n))
