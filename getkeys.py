from math import sqrt

def is_prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

