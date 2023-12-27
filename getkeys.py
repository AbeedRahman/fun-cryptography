from math import sqrt
import random


def is_prime(num):
    """Checks if argument is prime number.
    
    Args: 
        num: An integer.

    Returns: 
        True if num is prime, False otherwise.
    """
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def fi_N(p, q):
    return (p-1) * (q-1)


def gcd(a, b): 
    if (a == 0 or b == 0): 
        return 0
    if (a == b):
        return a
    if (a > b):  
        return gcd(a - b, b)   
    else:
        return gcd(a, b - a) 


def coprime(a, b):
    return gcd(a, b) == 1


def print_line():
    print("-" * 11)


print_line()
p = int(input("Enter a five digit prime number: "))

while not is_prime(p):
    p = int(input("Not a prime number. Please enter again: "))

print_line()
q = int(input("Enter another five digit prime number: "))

while not is_prime(q):
    q = int(input("Not a prime number. Please enter again: "))


N = p * q
fi = fi_N(p, q)
print("N = ", N)


e = random.randint(10e6, 10e7)
while not ( e < fi and coprime(e, fi) and coprime(e, N) ):
    e = random.randint(10e6, 10e7)
