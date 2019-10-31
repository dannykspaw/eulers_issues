'''
    Each new term in the Fibonacci sequence is generated
    by adding the previous two terms. By starting with 1
    and 2, the first 10 terms will be:
   
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence
    whose values do not exceed four million, find the sum
    of the even-valued terms.
'''
n = 1
x = [1, 2]
i = 0
while n < 4000000:
    x.append(x[i] + x[i+1])
    i = i + 1
    n = x[i+1]
sum = 0
for i in range(len(x)):
    if x[i] % 2 == 0:
        sum = sum + x[i]

print(f'''
         {x}
         {i}
         {n}
         {sum}
       ''')
