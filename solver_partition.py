#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)    

def divide_cities(cities):
    #find max x, y
    #find min x, y
    #if \x\ > \y\, sort height
    #else sort width
    max_x = list(max(cities))[0]
    min_x = list(min(cities))[0]
    max_y = list(max(cities, key = lambda x: x[1]))[1]
    min_y = list(min(cities, key = lambda x: x[1]))[1]
    if(max_x - min_x > max_y - min_y):
        cities = sorted(cities)
    else:
        cities = sorted(cities, key = lambda x: x[1])
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

def find_max_diff_point(pointer_list, city1, city2, common):
    max_diff = 0
    key = 0
    for i in range(4):
        p1 = pointer_list[i][0]
        p2 = pointer_list[i][1]
        diff = diff_distance(city1[p1], common, city2[p2])
        if(diff > max_diff):
            max_diff = diff
            key = i
    return key

def connect_cities(city1, city2):
    common_index1, common_index2, common = find_common_index(list(city1), list(city2))
    pointer1_1, pointer1_2 = find_exchange_pointer(city1, common_index1);
    pointer2_1, pointer2_2 = find_exchange_pointer(city2, common_index2);
    pointer_list = [[pointer1_1, pointer2_1], [pointer1_1, pointer2_2], [pointer1_2, pointer2_1], [pointer1_2, pointer2_2]]

    #find change_point
    key = find_max_diff_point(pointer_list, city1, city2, common)

    #extract common from city2. it should return path
    path = []
    if(key % 2 == 0):
        point = pointer_list[key][1] + len(city2)
        for i in range(len(city2) - 1):
            path.append(city2[(point - i) % len(city2)])
    else:
        point = pointer_list[key][1]
        for i in range(len(city2) - 1):
            path.append(city2[(point + i) % len(city2)])

    #insert path to city1
    if(key < 2):
        point = pointer_list[key][0] + 1
        city1[point:point] = path
    else:
        point = pointer_list[key][0]
        path.reverse()
        city1[point:point] = path
    return city1

def solve(cities):
    N = len(cities)

    if(N <= 3):
        return cities
    else:
        first_harf_cities, latter_harf_cities = divide_cities(cities)
        result_first = solve(first_harf_cities)
        result_latter = solve(latter_harf_cities)
        """
        solution = connect_cities(result_first, result_latter)
        solution_path = []
        for i in range(len(solution)):
            solution_path.append(list(cities).index(solution[i]))
        return solution_path
        """
        return connect_cities(result_first, result_latter)

def match_index(city_index, solution):
    solution_index = []
    for i in range(len(solution)):
        solution_index.append(list(city_index).index(solution[i]))
    return solution_index

if __name__ == '__main__':
    assert len(sys.argv) > 1
    city = read_input(sys.argv[1])
    solution = solve(city)
    solution = match_index(city, solution)
    print_solution(solution)
"""
    solution_path = []
    for i in range(len(solution)):
        solution_path.append(list(city).index(solution[i]))
    print_solution(solution_path)
"""


