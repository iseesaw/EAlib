#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:05:31
# @Author  :
# @Link    :
# @Version : 1.0

import random
from ..basic import Individual

def basic_crossover(individual1, individual2):
    """
    :param individual1: pass
    :param individual2: pass
    :return: Individual Object, new individual after crossover
    LOOK:
        assert individual.gene_len == problem.size
        assert no repeat number in individual's gene
        assert the max number in individual's gene is problem.size - 1
        assert the min number in individual's gene is 0
    """
    index1 = random.randint(0, individual1.gene_len - 1)
    index2 = random.randint(index1, individual2.gene_len - 1)

    temp_gene = individual1.gene[index1:index2]
    new_gene = []

    cont = 0
    for g in individual1.gene:
        if cont == index1:
            new_gene.extend(temp_gene)
            cont += 1
        if g not in temp_gene:
            new_gene.append(g)
            cont += 1

    return Individual(new_gene)


def Order_Crossover(individual1, individual2):
    """TODO"""
    raise NotImplementedError


def PMX_Crossover(individual1, individual2):
    """TODO"""
    raise NotImplementedError


def Cy_cle_Crossover(individual1, individual2):
    """TODO"""
    raise NotImplementedError


def Edge_Recombination(individual1, individual2):
    """TODO"""
    raise NotImplementedError
