import pandas as pd
import numpy as np
import sys
import cProfile
import math

df = pd.read_csv('1mmod.csv', sep=',', header=None).to_numpy()


def primeFactors(n):
    i = 2
    factors = np.array([])
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors = np.append(factors, i)
    if n > 1:
        factors = np.append(factors, n)
    return factors


def getBaseRep(factors):
    fin = 0
    for c in enumerate(factors):
        fin += 10 ** int(list(np.where(df == c))[0][-1])
    return str(fin)[::-1]


def getRealRep(n):
    fin = 1
    for ax, c in enumerate(str(n)):
        if c != '0':
            fin *= df[ax] ** int(c)
    return fin


if __name__ == '__main__':
    print("Enter a number to get its prime representation")
    for line in sys.stdin:
        if line.rstrip() == 'q':
            break
        try:
            a = int(line)
            holder = a
            a = primeFactors(a)
            print(f'The Base Prime Representation of {holder} is {getBaseRep(a)}, {a}')
        except ValueError as e:
            print(e)
            print('The input must be a number')
    print("Exit")
