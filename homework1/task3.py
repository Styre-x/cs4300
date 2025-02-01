def zerofunc(num):
    if num > 0:
        return "GT"
    if num < 0:
        return "LT"
    if num == 0:
        return "EQ"

def factorial(n):
    for i in range(1,n):
        n += n * i
    return n

def forloop():
    primes = []
    print(factorial(10))
    for i in range(2, 30): # 30 should cover the first 10 prime numbers?
        if factorial(i-1) == -i % i:
            print(i)
            primes.append(i)
    print(primes)
    return primes
forloop()