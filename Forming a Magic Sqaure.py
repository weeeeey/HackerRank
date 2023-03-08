#!/bin/python3

import math
import os
import random
import re
import sys

from copy import deepcopy

def formingMagicSquare(s):
    # Write your code here
    a = []
    # 5는 항상 가운데
    # 2,4,6,8 은 항상 꼭지점
    # 1,3,7,9 는 항상 4방향

    # 1~9 총합 45=> 세 수를 뽑아서 항상 같은 값이 나오므로 /3 값인 15로 맞춤
    # 1~9 세 수 조합 모두 구해서 합이 15인 것 구했고 각 수마다 뽑힌 횟수 체크하니 5는 네번, 2,4,6,8은 세번, 나머지 두번
    
    a.append([[6,1,8],[7,5,3],[2,9,4]])
    a.append([[2,9,4],[7,5,3],[6,1,8]])
    a.append([[8,1,6],[3,5,7],[4,9,2]])
    a.append([[4,9,2],[3,5,7],[8,1,6]])
    for i in range(4):
        gr=deepcopy(a[i])
        for j in range(3):
            for k in range(j,3):
                gr[j][k],gr[k][j] = gr[k][j],gr[j][k]
        a.append(gr)

    result = 55
    for num in range(8):
        small = 0
        for i in range(3):
            for j in range(3):
                small += abs(a[num][i][j]-s[i][j])
        result = min(result,small)

    return result
                
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
    # fptr.write(str(result) + '\n')
# 
    # fptr.close()
