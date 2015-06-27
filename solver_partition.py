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
    common_set = set(city1).intersection(set(city2))
    common = list(common_set)[0]
    common_index1 = city1.index(common)
    common_index2 = city2.index(common)
    return common_index1, common_index2, common

def find_exchange_pointer(city, common_index):
    if(common_index == 0):
        return len(city) - 1, 1
    if(common_index == len(city) - 1):
        return len(city) - 2, 0
    return common_index - 1, common_index + 1

def diff_distance(point1, common, point2):
    return distance(point1, common) + distance(common, point2) - distance(point1, point2)

def connect_cities(city1, city2):
    common_index1, common_index2, common = find_common_index(list(city1), list(city2))
    pointer1_1, pointer1_2 = find_exchange_pointer(city1, common_index1);
    pointer2_1, pointer2_2 = find_exchange_pointer(city2, common_index2);
    pointer_list = [[pointer1_1, pointer2_1], [pointer1_1, pointer2_2], [pointer1_2, pointer2_1], [pointer1_2, pointer2_2]]

    max_diff = 0
    key = 0
    for i in range(4):
        p1 = pointer_list[i][0]
        p2 = pointer_list[i][1]
        diff = diff_distance(city1[p1], common, city2[p2])
        print diff
        if(diff > max_diff):
            max_diff = diff
            key = i
        #print pointer_list[i][1]
    print key, max_diff
    


def solve(cities):
    
    N = len(cities)

    if(N <= 3):
        return cities
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
