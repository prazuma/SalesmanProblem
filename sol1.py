#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input, write_solution

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def path_length(path, cities):
    path_len = 0
    for i in range(len(path)):
        if i == len(path) - 1:
            path_len += distance(cities[path[i]], cities[path[0]])
        else:
            path_len += distance(cities[path[i]], cities[path[i + 1]])
    return path_len

def fullsearch(cities):
    N = len(cities)
    global min_length, min_path
    min_length = 100000000
    min_path = []
    def fullsearch_sub(start, solution):
        global min_length, min_path
        dist = path_length(solution, cities)
        if dist > min_length:
            return
        if N == len(solution): 
            new_len = path_length(solution, cities)
            if(new_len < min_length):
               min_length = new_len
               min_path = solution[:]
        else:
           for current_city in range(N):
               if current_city not in solution:
                   solution.append(current_city)
                   fullsearch_sub(current_city + 1, solution)
                   solution.pop()
    for i in range(N):
        fullsearch_sub(i, min_path)
    return min_path               

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = fullsearch(read_input(sys.argv[1]))
    write_solution(solution)
    print_solution(solution)
