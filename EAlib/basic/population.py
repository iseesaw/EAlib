#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:02:42
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : 1.0

import random
from ..basic import Individual

import logging
logger = logging.getLogger('EAlib')


class Population(object):
    """
    The class to represent population which is composed of individual.
    """

    def __init__(self, problem, selection_func, crossover_func, mutation_func, elitism=True, unit_num=50, max_gen=100, prob_c=0.5, prob_m=0.3):
        """
        :param problem: TSPProblem object
        :param max_gen: max generations(iterations)
        :param unit_num: the number of individuals in the population
        :param prob_c: probability of crossover
        :param prob_m: probability of mutation
        """
        super(Population, self).__init__()

        self.problem = problem

        self.selection_func = selection_func
        self.crossover_func = crossover_func
        self.mutation_func = mutation_func

        self.elitism = elitism

        self.unit_num = unit_num
        self.max_gen = max_gen
        self.prob_c = prob_c
        self.prob_m = prob_m

        self.best_ones = []

        self._initPopulation()

        self.generations = 1

    def _initPopulation(self):
        """init the population in O(n)"""
        self.individuals = []
        for i in range(self.unit_num):
            # full arrangement
            gene = [x for x in range(self.problem.size)]
            # shuffle and create a Individual object
            random.shuffle(gene)
            self.individuals.append(Individual(gene))

    def judge(self):
        """
        insert the best individual of the last generation to next generation.
        :return:
        """
        temp = -1
        best_one = None
        for individual in self.individuals:
            distance = self.get_disctance(individual)
            if temp == -1 or distance < temp:
                temp = distance
                best_one = individual

        self.best_ones.append(best_one)

    def get_disctance(self, individual):
        """
        calculate the fitness(cost) of the given individual.
        :param individual:
        :return:
        """
        if individual.fitness:
            return individual.fitness
        distance = 0
        for i in range(self.problem.size - 1):
            distance += self.problem.DM[individual.gene[i]
                                        ][individual.gene[i + 1]]
        distance += self.problem.DM[individual.gene[
            self.problem.size - 1]][individual.gene[0]]
        individual.set_fitness(distance)

        return distance

    def next(self):
        """next
        :param selection_func:
        :param crossover_func:
        :param mutation_func:
        get a new generation as the following procedure.
        judge -> selection -> mutation -> crossover -> judge
        """
        self.judge()

        new_individuals = []

        if self.elitism:
            new_individuals.append(self.best_ones[-1])

        # next generations
        for _ in range((self.unit_num - 1) if self.elitism else self.unit_num):
            # select the first parent
            parent1 = self.selection_func(self)

            # crossover
            rate_c = random.random()
            if rate_c < self.prob_c:
                parent2 = self.selection_func(self)
                individual = self.crossover_func(parent1, parent2)
            else:
                individual = parent1

            # mutation
            rate_m = random.random()
            if rate_m < self.prob_m:
                individual = self.mutation_func(individual)

            # TODO
            self._eval(individual)
            new_individuals.append(individual)

        # update
        self.individuals = new_individuals
        self.generations += 1

    def _eval(self, individual):
        """
        individual.gen_len = self.problem.size
        len(set(individual.gen_len)) = self.problem.size
        max(set(individual.gene)) = individual
        """
        gene_set = set(individual.gene)
        assert len(gene_set) == self.problem.size, f"gene size ({len(gene_set)}) != problem size ({self.problem.size})"

        gene_max, gene_min = max(gene_set), min(gene_set)
        assert gene_max == self.problem.size - 1, f"gene_max ({gene_max}) != problem size ({self.problem.size})"
        assert gene_min == 0, f"gene min ({gene_min})"

    def evolve(self, print_every):
        """
        get descendants of now generation many time.
        :param print_every:
        :return:
        """
        for idx in range(self.max_gen):
            self.next()
            if not idx % print_every:
                logger.info(f"{idx}th\n" + str(self.best_ones[-1].fitness))
