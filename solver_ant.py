# -*- coding: utf-8 -*-
import numpy
import random
from random import randrange
import math
import sys
from ant import Ant
from common import print_solution, read_input

ALPHA = 1.0
BETA = 5.0
RHO = 0.5
Q = 100

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def get_dists(cities):
    N = len(cities)
    dists = numpy.zeros(shape = (N, N))
    for i in range(N):
        for j in range(i, N):
            dist = 0
            if i != j:
                dist = distance(cities[i], cities[j])
            dists[i][j] = dists[j][i] = dist
    return dists

def get_phers(cities):#フェロモンの初期化
    N = len(cities)
    phers = numpy.empty(shape = (N, N))
    phers[:] = 0.1#本当は、greedyで、全ての別の都市をスタート地点とした経路を都市のあk図だけ作り、その平均をとったもの
    return phers

def get_ants(num_ant, fields):
    #都市の数と同じ蟻を用意
    #それぞれランダムに都市を割り当て配置する。
    #繰り返し回数(t) = 0とする
    ants = []
    for i in range(num_ant):
        initial_city = numpy.random.randint(0, num_ant)
        print initial_city
        ant = Ant(initial_city, fields, ALPHA, BETA)
        ants.append(ant)
    return ants

def solve(cities):
    dists = get_dists(cities)
    phers = get_phers(cities)
    fields = dict(
        cities = cities,
        dists = dists,
        phers = phers
    )
    ants = get_ants(len(cities), fields)
    return ants

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    #print_solution(solution)
