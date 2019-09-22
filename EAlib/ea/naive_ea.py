#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:08:09
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : 1.0

from ..basic import Individual, Population, TSPProblem
from ..utils import BasicLoader
from ..operators.mutation import basic_mutation
from ..operators.crossover import basic_crossover
from ..operators.selection import basic_selection

class Naive_Ea(object):
    """docstring for Naive_Ea"""
    def __init__(self, filename):
        super(Naive_Ea, self).__init__()
        
        self._test()
        self.tsp = TSPProblem(mode=2, dataloader=BasicLoader(filename))

        self.population = Population(self.tsp, basic_selection, basic_crossover, basic_mutation)
        self.population.evolve(print_every=50)

    def _test(self):
        print("hello")


if __name__ == '__main__':
    Naive_Ea("tsp/att48.tsp")