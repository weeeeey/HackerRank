#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(n,arr):
    for i in range(n//2):
        arr[i]+=" "
    
    # arr.sort(key=lambda x:int(x[0]))
    # result = []    
    # for i in range(n):
        # result.append(arr[i][1])
    # print(" ".join(result))

    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(n,arr)
