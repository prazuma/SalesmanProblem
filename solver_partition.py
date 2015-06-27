#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)    

def divide_cities(cities):
    cities = sorted(cities)
    n = len(cities) / 2
    first_harf_cities = cities[:n + 1]
    latter_harf_cities = cities[n:]
    return first_harf_cities, latter_harf_cities

def find_common_index(city1, city2):
    common = set(city1).intersection(set(city2))
    common_index1 = city1.index(list(common)[0])
    common_index2 = city2.index(list(common)[0])
    return common_index1, common_index2

def connect_cities(city1, city2):
    common_index1, common_index2 = find_common_index(list(city1), list(city2))
    print common_index1
    print common_index2
    d1 = distance(city1[common_index1 - 1], city1[common_index1]) + distance(city2[common_index2], city2[common_index2 + 1]) - distance(city1[common_index1 - 1], city2[common_index2 + 1])



def solve(cities):
    
    N = len(cities)

    if(N <= 3):
        print "---"
    else:
        first_harf_cities, latter_harf_cities = divide_cities(cities)
        result_first = solve(first_harf_cities)
        result_latter = solve(latter_harf_cities)
        connect_cities(result_first, result_latter)

    """
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
"""
    #return solution
    return cities


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solve(read_input(sys.argv[1]))
    #solution = solve(read_input(sys.argv[1]))
    #print_solution(solution)
