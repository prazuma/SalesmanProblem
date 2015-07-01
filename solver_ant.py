# -*- coding: utf-8 -*-
import numpy
import random
from random import randrange
import math
import sys
from ant import Ant
from common import print_solution, read_input

ALPHA = 1.0#蟻が出すフェロモンの量
BETA = 0.5#都市間距離の重要度を決めるパラメータ
RHO = 0.5#フェロモンの蒸発率
Q = 1

MAX_RUN = 10 #この値が大きければ大きいほど値は良くなる

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
        ant = Ant(initial_city, fields, ALPHA, BETA)
        ants.append(ant)
    return ants

def evaporate_pheromon(pheromon):
    pheromon *= (1.0 - RHO)
    return pheromon

#蟻kが繰り返し回数tの時に落とすフェロモンの量
def delta_pheromon(path_len):
    delta = Q / path_len
    return delta

def update_pheromons(fields, ants):
    
    for i in range(len(fields['cities'])):
        for j in range(i, len(fields['cities'])):
            if i != j:
                pheromon = evaporate_pheromon(fields['phers'][i][j])
                fields['phers'][i][j] = fields['phers'][j][i] = pheromon
                
    for ant in ants:
        for i in range(len(ant.path)):
            f = ant.path[i]
            t = ant.path[i - 1]
            delta = delta_pheromon(ant.path_len)
            fields['phers'][f][t] += delta
            fields['phers'][f][t] = fields['phers'][t][f]

def start(fields, ants):
    best_ant = None
    min_len = 1000000000
    for i in range(MAX_RUN):
        update_pheromons(fields, ants)
        for ant in ants:
            ant.run()
            if ant.path_len < min_len:
                best_ant = ant
                min_len = ant.path_len
    return best_ant


def solve(cities):
    dists = get_dists(cities)
    phers = get_phers(cities)
    fields = dict(
        cities = cities,
        dists = dists,
        phers = phers
    )
    ants = get_ants(len(cities), fields)
    best_ant = start(fields, ants)
    return best_ant

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution.path)
