"""Encrypts a sentance using a key pair.
Usage: python encrypt.py <private_keyfile> <message>
"""

__author__ = 'Misnad'

import sys

# def to_num(words):
#     num = ""
#     for i in words:
#         num = num + str(ord(i) - 23)
#     return num


def to_num(words):
    """Converts a sentance to an integer that can be reverted back using to_word().

    Args:
      words: A sentance containg english alphabets and spaces.

    Returns:
      The integer corresponding to the sentance.

    Raises:
      ConnectionError: If no available port is found.
    """
    # TODO catch if (ord(i) - 23) > 99
    num = 0
    for i in words:
        num = num*100 + ord(i) - 23
    return num


def to_word(num):
    word = ""
    while num:
        word = chr((num%100) + 23)  + word
        num = num // 100
    return word


with open(sys.argv[1], 'r') as keyfile:
    # TODO catch invalid key file
    d = int(keyfile.readline())
    n = int(keyfile.readline())

cyper = int(sys.argv[2])

message = to_word(((cyper) ** d) % n)
print("Your message is:", message)
