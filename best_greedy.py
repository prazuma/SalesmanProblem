#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    #current_city = 0
    def find_next_city(current_city, cities):
        def distance_from_current_city(to):
            #print(current_city)
            return dist[current_city][to]
        return min(cities, key = distance_from_current_city)

    def get_solution(start):
        current_city = start
        unvisited_cities = set(range(0, N))
        unvisited_cities.remove(start)
        solution = [0, current_city]

        while unvisited_cities:
            next_city = find_next_city(current_city, unvisited_cities)
            unvisited_cities.remove(next_city)
            solution.append(next_city)
            solution[0] += dist[current_city][next_city]
            current_city = next_city
        solution[0] += dist[start][current_city]
        return solution

    path_len = 0
    for i in range(N):
        path = get_solution(i)
        if(path_len == 0 or path[0]<path_len):
            path_len = path[0]
            solution = path[1:]
    return solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
