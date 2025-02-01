def zerofunc(num):
    if num > 0:
        return "GT"
    if num < 0:
        return "LT"
    if num == 0:
        return "EQ"

def prime(num):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       return num

def forloop():
    primes = []
    for num in range(2,101):
        primeNum = prime(num)
        if primeNum:
            primes.append(primeNum)
    return primes

def sum0100():
    sum = 0
    for i in range(0,101):
        sum += i
    return sum

def test_all():
    assert zerofunc(0) == "EQ"
    assert zerofunc(10) == "GT"
    assert zerofunc(-10) == "LT"
    assert forloop() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert sum0100() == 5050