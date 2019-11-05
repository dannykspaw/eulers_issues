import math

def prime_finder(n):
    if n == 1:
        return False
    if n == 2: 
        return True
    if n % 2 == 0:
        return False
    divisor = math.floor(math.sqrt(n))
    if n > 2:
        for i in range(3, 1 + divisor, 2):
            if n % i == 0:
                return False
        return True
print(prime_finder(104729))

x = int(input("User input number:\n"))
for i in range(x, 3, -2):
    if prime_finder(i) == True:
        print(i)
        break
print('The number is prime and has no prime factors.')

prime_factors = []
for i in range(2, x):
    if (
        x % i == 0 and prime_finder(i) == True
        ):
        prime_factors.append(i)
        print(i)
        product = 1
        for i in range(len(prime_factors)):
            product = product * prime_factors[i]
            if product == x:
                break
        

