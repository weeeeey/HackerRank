#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

INF = int(1e5)+1
def roadsAndLibraries(n, c_lib, c_road, cities):
    visited = [False]*INF                
    gr = [[] for i in range(INF)]
    for c in cities:
        s,e = c 
        gr[s].append(e)
        gr[e].append(s)
    q = deque()
    body = 0    #빌딩 최소 갯수 구하기
    road = 0 
    c = 0    #다른 도시랑 이어지지 않는 시티 갯수 판별하기
    for city in cities:
        start = city[0]
        if visited[start]==True:
            continue
        body+=1 
        visited[start]=True
        c+=1
        q=deque()
        q.append(start)
        while(q):
            cur = q.popleft()
            for next in gr[cur]:
                if visited[next]==True:
                    continue
                visited[next]=True
                q.append(next)
                road+=1
                c+=1
    if(n*c_lib < (body*c_lib+road*c_road+(n-c)*c_lib)):
        return n*c_lib      #도로 짓는 것보다 빌딩만 세웠을 떄 최솟값
    else:
        return body*c_lib+road*c_road+(n-c)*c_lib    #최소 빌딩 갯수+ 최대 로드(중복x)+도로 없는 도시  
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        if(m==0):
            result = n*c_lib   
        else:
            result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
