import pandas as pd
import numpy as np
import sys

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


def getBaseRep(n):
    fin = 0
    finStr = ''
    factors = primeFactors(n)
    for ax, b in enumerate(df):
        fin += np.count_nonzero(factors == b) * (10 ** ax)
        finStr = str(fin)[::-1]
        if getRealRep(finStr) == n:
            break
    return finStr


def getRealRep(n):
    fin = 1
    for ax, c in enumerate(str(n)):
        if c != '0':
            fin *= df[ax] ** int(c)
    return fin


if __name__ == '__main__':
    for line in sys.stdin:
        if line.rstrip() == 'q':
            break
        try:
            a = int(line)
            print(f'The Base Prime Representation of {a} is {getBaseRep(a)}, {primeFactors(a)}')
        except ValueError:
            print('The input must be a number')

    print("Exit")
