#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input, write_solution


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    def find_next_city(current_city, cities):
        def distance_from_current_city(to):
            return dist[current_city][to]
        return min(cities, key = distance_from_current_city)

    def get_solution(start):
        current_city = start
        unvisited_cities = set(range(0, N))
        unvisited_cities.remove(start)
        solution = [current_city]

        while unvisited_cities:
            next_city = find_next_city(current_city, unvisited_cities)
            unvisited_cities.remove(next_city)
            solution.append(next_city)
            current_city = next_city
        solution.append(start)
        return solution

        
    def do_2opt(solution):    
        for i in range(len(solution) - 1):
            for j in range(i+2, len(solution)):
                j2 = j + 1
                if(j2 == len(solution)):
                    j2 = 0
                diff = distance(cities[solution[i]], cities[solution[i + 1]]) + distance(cities[solution[j]], cities[solution[j2]]) - distance(cities[solution[i]], cities[solution[j]]) - distance(cities[solution[i + 1]], cities[solution[j2]])
                if(diff > 0):
                    exchange_path = solution[i+1:j2]
                    exchange_path.reverse()
                    solution[i+1:j2] = exchange_path
        return solution
    
    
    path_len = 0
    for i in range(N):
        path = get_solution(i)
        path1 = do_2opt(path)
        length = 0
        for n in range(0, N):
            length += dist[path[n]][path[n+1]]
        print(length)
        if(path_len == 0 or length<path_len):
            path_len = length
            solution = path
    print(path_len)
    solution.pop(len(solution)-1)
    return solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    write_solution(solution)
    print_solution(solution)
