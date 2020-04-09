#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    m2, m3 = {}, {}
    ans = 0
    for n in arr:
       # print m2, m3, ans
        nr = int(n * r)
        if m3.has_key(n):
            ans += m3[n]
        if m2.has_key(n):
            m3[nr] = m3[nr] + m2[n] if m3.has_key(nr) else m2[n]
        m2[nr] = m2[nr] + 1 if m2.has_key(nr) else 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = raw_input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = map(long, raw_input().rstrip().split())

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
