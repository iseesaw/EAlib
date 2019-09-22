#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:05:42
# @Author  :
# @Link    :
# @Version : 1.0

import copy
import random

from ..basic import Individual

def basic_mutation(individual):
    """
    :param individual: Individual Object
    :return: Individual Object, new individual after gene mutation
    """
    index1 = random.randint(0, individual.gene_len - 1)
    index2 = random.randint(0, individual.gene_len - 1)

    # Don't change the origin population!!!
    new_gene = copy.deepcopy(individual.gene)

    new_gene[index1], new_gene[index2] = new_gene[index2], new_gene[index1]

    return Individual(new_gene)



def insert_mutation():
    """TODO"""
    raise NotImplementedError


def swap_mutation():
    """TODO"""
    raise NotImplementedError


def inversion_mutation():
    """TODO"""
    raise NotImplementedError


def scramble_mutation():
    """TODO"""
    raise NotImplementedError
