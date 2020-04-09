#!/bin/python

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    m,c = {}, {}
    m = defaultdict(lambda:0,m)
    c = defaultdict(lambda:0,c)
    ans = []
    for q, z in queries:
        if q == 1:
            c[m[z]] = max(0, c[m[z]] - 1)
            m[z] = m[z] + 1
            c[m[z]] += 1
        elif q == 2:
            c[m[z]] = max(0, c[m[z]] - 1)
            m[z] = max(0, m[z] - 1)
            c[m[z]] += (m[z] > 0)
        elif q == 3:
            ans.append(int(c[z] > 0))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    queries = []

    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
