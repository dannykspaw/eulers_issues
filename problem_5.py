n = 20
i = 1
while i < 21:
    if n % i == 0:
        i = i + 1
    else:
        n = n + 20
        i = 1
        print(n)
print(n)
