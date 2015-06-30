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

    def remove_intersection(solution):
        i = -1
        while i<len(solution)-3:
            i += 1
            point1, point2 = cities[solution[i]], cities[solution[i+1]]
            n = i+2
            while n<len(solution)-1:
                point3, point4 = cities[solution[n]], cities[solution[n+1]]
                ta = (point3[0] - point4[0])*(point1[1] - point3[1]) + (point3[1] - point4[1])*(point3[0] - point1[0])
                tb = (point3[0] - point4[0])*(point2[1] - point3[1]) + (point3[1] - point4[1])*(point3[0] - point2[0])
                tc = (point1[0] - point2[0])*(point3[1] - point1[1]) + (point1[1] - point2[1])*(point1[0] - point3[0])
                td = (point1[0] - point2[0])*(point4[1] - point1[1]) + (point1[1] - point2[1])*(point1[0] - point4[0])
                if(ta*tb<0 and tc*td<0):
                    #print(solution[i])
                    temp = solution[i+1]
                    solution[i+1] = solution[n]
                    solution[n] = temp
                    #print(solution[n])
                #if(i == 0 or n+1 == N)
                n += 1
        return solution

    path_len = 0
    for i in range(N):
        path = get_solution(i)
        #path1 = remove_intersection(path)
        #while (path != path1):
            #path = path1
            #path1 = remove_intersection(path1)
        length = 0
        for n in range(0, N):
            length += dist[path[n]][path[n+1]]
        #length += dist[path[0]][path[N-1]]
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
    print_solution(solution)
