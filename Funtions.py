import sys

k = [1, 3, 6]


def modify(k):
    k.append(39)
    print(k)


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def printlist(liste):
    for item in liste:
        print(item)
