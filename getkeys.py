from math import sqrt
import random


#TODO pre-compute and store computed prime numbers prime numbers.
def is_prime(num):
    """Checks if argument is prime number.
    
    Args: 
        num: An integer.

    Returns: 
        True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def fi(p, q):
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


def extended_gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) of two integers and expresses it as a linear combination of the numbers using the Extended Euclidean Algorithm.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        A tuple containing:
            - gcd: The greatest common divisor of a and b.
            - x: The coefficient for a in the linear combination.
            - y: The coefficient for b in the linear combination.
    """
    if a == 0:
        return (b, 0, 1)
    
    g, x, y = extended_gcd(b % a, a)
    return (g, y - (b // a) * x, x)


def mod_inverse(e, phi_n):
    g, x, _ = extended_gcd(e, phi_n)
    if g != 1:
        raise ValueError("The inverse does not exist.")
    else:
        return x % phi_n


def print_line():
    print("-" * 11)


print_line()
name = input("Enter your nickname: ")

print_line()
while True:
    p = int(input("Enter a six-digit prime number (p): "))
    # if 100000 <= p <= 999999 and is_prime(p):
    if is_prime(p):
        break
    else:
        print("Not a prime number or not six digits. Please enter again:")

print_line()
while True:
    q = int(input("Enter a six-digit prime number (q): "))
    # if 100000 <= p <= 999999 and is_prime(p):
    if is_prime(q):
        break
    else:
        print("Not a prime number or not six digits. Please enter again:")


N = p * q
fi_N = fi(p, q)
print("N = ", N)

e = 65537

d = mod_inverse(e, fi_N)
print("Private exponent (d):", d)

# creates a publickey and privatekey file
f = open(name + "-publickey", 'w')
f.write(str(e) + "\n" + str(N))
f.close()

f = open(name + "-privatekey", 'w')
f.write(str(d) + "\n" + str(N))
f.close()
