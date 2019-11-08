x = input('User input a number:\n')
print(x[::-1])

list = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        val = str(i*j)
        if val == val[::-1]:
            print(val)
            print(i, j)
            list.append(int(val))
print(max(list))
