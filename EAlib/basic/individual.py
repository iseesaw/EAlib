#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:02:34
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : 1.0


class Individual(object):
    """
    The class to represent individual.
    """

    def __init__(self, gene):
        """
        :param gene: List, the gene of the individual, full permutation of cities, an optional solution
        """
        super(Individual, self).__init__()

        self.gene = gene

        self.gene_len = len(gene)

        self.fitness = None

    def set_fitness(self, fitness):
        """
        :param fitness: int,
        """
        self.fitness = fitness

    def __repr__(self):
        return f"Fitness {self.fitness}\nGene {self.gene}"
