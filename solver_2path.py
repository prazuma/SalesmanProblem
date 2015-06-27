#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities, first_city_index):
    N = len(cities)

    cities[0], cities[first_city_index] = cities[first_city_index], cities[0]
    
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]
    i = 0
    front = 1
    rear = 0

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        if i % 2 == 0:
            solution.insert(front, next_city)
            front += 1
            current_city = solution[rear - 1]
        else:
            solution.insert(len(solution) - rear, next_city)
            rear += 1
            current_city = solution[front - 1]
        i += 1
        #current_city = next_city
    return solution

def solve_all(cities):
    n = len(cities)
    min_length = 1000000000
    min_solution = []
    for i in range(n):
        solution = solve(list(cities), i)
        path_length = sum(distance(cities[u], cities[v])
                          for u, v in zip(solution, solution[1:] + solution[0:1]))
        if(path_length < min_length):
            min_length = path_length
            min_solution = solution
    print min_length
    return min_solution

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]), 0)
    #solution = solve_all(read_input(sys.argv[1]))
    print_solution(solution)
