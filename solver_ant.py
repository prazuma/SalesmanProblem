# -*- coding: utf-8 -*-
import numpy
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

def get_phers(cities):#フェロモンの初期化
    N = len(cities)
    phers = numpy.empty(shape=(N, N))
    phers[:] = 0.1#本当は、greedyで、全ての別の都市をスタート地点とした経路を都市のあk図だけ作り、その平均をとったもの
    return phers

def solve(cities):
    phers = get_phers(cities)
    return phers

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
