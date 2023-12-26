from math import sqrt

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


n = p * q
print("N = ", n)


def fi_N(p, q):
    return (p-1) * (q-1)


