#!/bin/python3

import math
import os
import random
import re
import sys

# 주어진 무한개의 동전으로 n을 표현할 수 있는 방법의 수를 출력하면 됨.
# 1~n을 세로열로 두고 
# 동전을 오름차순으로 정렬한 뒤 가장 낮은 단위부터 하나씩 채움
# 첫 동전의 배수들은 모두 1로 채움 + 각 줄의 각 동전 1개일때 1로 채움
# 귀납식: a(i,j)=a(i-1,j)+a(i,j-coin)+a(i,j)

def getWays(n, c):
    # Write your code here
    gr = [[0]*(n+1) for i in range(len(c))]
    c.sort()
    num = len(c)
    for i in range(1,(n//c[0])+1):
        gr[0][i*c[0]]=1
    for i in range(1,num):
        if(c[i]>n):
            break       #coin자체가 구할려는 n보다 클때는 0이니까 무시
        gr[i][c[i]]=1
    for i in range(1,num):
        k = c[i]
        if k>n:
            gr[i][-1]=gr[i-1][-1]
            continue
        for j in range(1,n+1):
            if(j-k<0):
                gr[i][j]=gr[i-1][j]+gr[i][j]    
            else:
                gr[i][j]=gr[i-1][j]+gr[i][j-k]+gr[i][j]
    
    return gr[-1][-1]
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    print(ways)
    # fptr.write(str(ways) + '\n')

    # fptr.close()
