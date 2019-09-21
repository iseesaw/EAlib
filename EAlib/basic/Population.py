#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:02:42
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : 1.0


class Population(object):
    """docstring for Population"""

    def __init__(self, problem, unit_num, max_gen, prob_c, prob_m):
        """
        :param problem: TSPProblem object
        :param max_gen: max generations(iterations)
        :param unit_num: the number of individuals in the population
        :param prob_c: probability of crossover
        :param prob_m: probability of mutation
        """
        super(Population, self).__init__()

        self.problem = problem

        self.unit_num = unit_num
        self.max_gen = max_gen
        self.prob_c = prob_c
        self.prob_m = prob_m

        self.best_ones = []

    def initPopulation(self):
        """init the population in O(n)"""

    def evolve(self):
        """evolve
        judge -> selection -> mutation -> crossover -> judge
        """
