#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input, write_solution


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)    

def city_pattern(city):
    max_x = list(max(city))[0]
    min_x = list(min(city))[0]
    max_y = list(max(city, key = lambda x: x[1]))[1]
    min_y = list(min(city, key = lambda x: x[1]))[1]
    return max_x - min_x > max_y - min_y

def divide_cities(cities):
    if(city_pattern(cities)):
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

def remove_common(city, point, key):
    path = []
    if(key % 2 == 0):
        point += len(city)
        for i in range(len(city) - 1):
            path.append(city[(point - i) % len(city)])
    else:
        for i in range(len(city) - 1):
            path.append(city[(point + i) % len(city)])
    return path

def insert_path_city(city, point, path, key):
    if(key < 2):
        point += 1
        city[point:point] = path
    else:
        path.reverse()
        city[point:point] = path
    return city

def connect_cities(city1, city2):
    common_index1, common_index2, common = find_common_index(list(city1), list(city2))
    pointer1_1, pointer1_2 = find_exchange_pointer(city1, common_index1);
    pointer2_1, pointer2_2 = find_exchange_pointer(city2, common_index2);
    pointer_list = [[pointer1_1, pointer2_1], [pointer1_1, pointer2_2], [pointer1_2, pointer2_1], [pointer1_2, pointer2_2]]

    #find change_point
    key = find_max_diff_point(pointer_list, city1, city2, common)

    #remove common_city from city2. it should return correct path
    path = remove_common(city2, pointer_list[key][1], key)
    
    city1 = insert_path_city(list(city1), pointer_list[key][0], path, key)

    return city1

def solve(cities):
    N = len(cities)

    if(N <= 3):
        return cities
    else:
        first_harf_cities, latter_harf_cities = divide_cities(cities)
        result_first = solve(first_harf_cities)
        result_latter = solve(latter_harf_cities)
        return connect_cities(result_first, result_latter)

def do_2opt(solution):    
    for i in range(len(solution) - 1):
        for j in range(i+2, len(solution)):
            j2 = j + 1
            if(j2 == len(solution)):
                j2 = 0
            diff = distance(solution[i], solution[i + 1]) + distance(solution[j], solution[j2]) - distance(solution[i], solution[j]) - distance(solution[i + 1], solution[j2])
            if(diff > 0):
                exchange_path = solution[i+1:j2]
                exchange_path.reverse()
                solution[i+1:j2] = exchange_path
    return solution
    
def match_index(city_index, solution):
    solution_index = []
    for i in range(len(solution)):
        solution_index.append(list(city_index).index(solution[i]))
    return solution_index

def lin_kernighan(cities):
    min_len = 10000000
    base = 0
    N = len(cities)
    for i in range(N):
        i1 = i
        i2 = (i + 1) % N
        i3 = (i + 2) % N
        length = distance(cities[i1], cities[i2]) + distance(cities[i2], cities[i3])
        if(length < min_len):
            min_len = length
            base = i
    count = 0
    for probe in range(base + 3, N):
        print "probe: ",
        print probe
        next_probe = (probe + 1) % N
        if(count == 0):
            delta = distance(cities[base], cities[base + 1]) - distance(cities[base + 1], cities[next_probe])
        elif(count == 1):
            delta = distance(cities[base], cities[base + 1]) + delta - distance(cities[base + 1], cities[next_probe])
        else:
            delta = distance(cities[base], cities[base + 1]) + distance(cities[probe], cities[next_probe]) - distance(cities[base], cities[probe]) - distance(cities[base + 1], cities[next_probe]) + delta

        count += 1
        print delta
                

if __name__ == '__main__':
    assert len(sys.argv) > 1
    city = read_input(sys.argv[1])
    solution = solve(city)
    solution = do_2opt(solution)
    lin_kernighan(solution)
    solution = match_index(city, solution)
    write_solution(solution)
    print_solution(solution)


