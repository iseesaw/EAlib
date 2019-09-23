#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:05:42
# @Author  : Yangfan Li (yfli@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
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


def insert_mutation(individual):
    """
    :param individual: Individual Object
    :return: Individual Object, new individual after gene mutation
    """
    index1 = random.randint(0, individual.gene_len - 1)
    index2 = random.randint(0, individual.gene_len - 1)
    index1 = min(index1, index2)
    index2 = max(index1, index2)

    new_gene = copy.deepcopy(individual.gene)

    temp_value = new_gene.pop(index2)
    new_gene.insert(index1, temp_value)

    return Individual(new_gene)


def swap_mutation(individual):
    """
    :param individual: Individual Object
    :return: Individual Object, new individual after gene mutation
    """
    return basic_mutation(individual)


def inversion_mutation(individual):
    """
    :param individual: Individual Object
    :return: Individual Object, new individual after gene mutation
    """
    index1 = random.randint(0, individual.gene_len - 1)
    index2 = random.randint(0, individual.gene_len - 1)
    index1 = min(index1, index2)
    index2 = max(index1, index2)

    new_gene = copy.deepcopy(individual.gene)

    new_gene[index1, index2+1] = list(reversed(new_gene[index1, index2+1]))

    return Individual(new_gene)


def scramble_mutation(individual):
    """
    :param individual: Individual Object
    :return: Individual Object, new individual after gene mutation
    """
    index1 = random.randint(0, individual.gene_len - 1)
    index2 = random.randint(0, individual.gene_len - 1)
    index1 = min(index1, index2)
    index2 = max(index1, index2)

    new_gene = copy.deepcopy(individual.gene)

    temp_list = new_gene[index1, index2+1]
    temp_list.shuffle(temp_list)
    new_gene[index1, index2+1] = temp_list

    return new_gene
