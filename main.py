import pandas as pd
import numpy as np
import sys

df = pd.read_csv('1mmod.csv', sep=',', header=None).to_numpy()
np.set_printoptions(suppress=True)


def primeFactors(n):
    i = 2
    factorsB = np.array([])
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factorsB = np.append(factorsB, i)
    if n > 1:
        factorsB = np.append(factorsB, n)
    return factorsB


def compressBaseRep(fin):
    finMod = ""
    counter = 0
    for d in str(fin):
        if d != '0':
            if counter > 0:
                finMod += '(' + str(counter) + ')'
                counter = 0
            finMod += d
        else:
            counter += 1
    if str(fin)[-1] == '0':
        counter = 0
        for ar in str(fin)[::-1]:
            if ar == '0':
                counter += 1
            else:
                finMod += '(' + str(counter) + ')'
                break
    return finMod


def decompressBaseRep(n):
    nTwo = ""
    baseHolder = 0
    for rx, r in enumerate(str(n)):
        if r == '(':
            baseHolder = rx
        elif r == ')':
            for router in range(int(str(n)[baseHolder + 1:rx])):
                nTwo += '0'
            baseHolder = 0
        elif baseHolder == 0:
            nTwo += r
    return nTwo


def getBaseRep(factorsA):
    fin = 0
    for c in factorsA:
        fin += 10 ** int(list(np.where(df == c))[0][-1])
    return fin


def getRealRep(n):
    fin = 1
    for ax, c in enumerate(str(n)[::-1]):
        if c != '0':
            fin *= df[ax] ** int(c)
    return fin


def runTest():
    fin = np.array([])
    goodFin = np.array([])
    maxi = 5000
    average = 0
    for t in range(0, maxi):
        print(t)
        newest = sys.getsizeof(str(t)) - sys.getsizeof(compressBaseRep(getBaseRep(primeFactors(t))))
        average += newest
        fin = np.append(fin, newest)
        if newest >= 0:
            goodFin = np.append(goodFin, t)
    print(fin)
    print(goodFin)
    print(average / maxi)


if __name__ == '__main__':
    print("Enter a number to get its prime representation")
    print(
        "The number must not contain a factor that is represented as n^10>, i.e. 2^10> will not be represented properly, nor will 3^10>")
    factors = ""
    for line in sys.stdin:
        if line.rstrip() == 'q':
            break
        if line.rstrip() == 't':
            runTest()
            break
        try:
            a = int(line)
            holder = a
            a = primeFactors(a)
            factors = a
            a = getBaseRep(a)
            print(f'The Base Prime Representation of {holder} is {a}, {factors}')
            compressedVer = compressBaseRep(a)
            print(f'The compressed version is {compressedVer}')
            print(f'This saves {sys.getsizeof(str(holder)) - sys.getsizeof(compressedVer)} bytes of data')
        except ValueError:
            print('The input must be a number')
        except IndexError:
            print(f'The input is too large to represent as its prime factors are {factors}')
    print("Exit")
