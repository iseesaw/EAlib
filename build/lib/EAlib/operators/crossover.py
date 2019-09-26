#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:05:31
# @Author  : wjm
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
    # order 1 crossover

    # # select a random swath of consecutive alleles from parent 1.
    # index1 = random.randint(0, individual1.gene_len - 1)
    # index2 = random.randint(index1, individual1.gene_len - 1)

    # # drop down to child 1.
    # temp_gene = individual1.gene[index1:(index2+1)]
    # new_gene = []

    # # Starting on the right side of the swath,
    # # grab alleles from parent 2 and insert them in Child 1
    # # at the right edge of the swath.

    # cont = 0
    # for g in individual2.gene:
    #     if g not in temp_gene:
    #         new_gene.append(g)
    #         cont += 1
    #     if cont == index1:
    #         new_gene.extend(temp_gene)
    #         cont += 1

    # return Individual(new_gene)
    return basic_crossover(individual1, individual2)

def PMX_Crossover(individual1, individual2):

    # copy a random swath of consecutive alleles from Parent 1 to the Child
    index1 = random.randint(0, individual1.gene_len - 1)
    index2 = random.randint(index1, individual1.gene_len - 1)

    temp_gene = individual1.gene[index1:index2 + 1]
    new_gene = [-1] * individual1.gene_len

    for i in range(index1, index2 + 1):
        new_gene[i] = individual1.gene[i]

    # select each value that hasn't been copied to child from same segment positions of parent2
    for i in range(index1, index2 + 1):
        tmp = individual2.gene[i]
        if tmp not in temp_gene:
            # i. Locate the value, V, from parent 1 in this same position.
            V = individual1.gene[i]
            # ii. Locate the same value in parent 2.
            pos = individual2.gene.index(V)
            # if the index is part of the swath, goto i, loop until find a position
            while(pos in range(index1, index2 + 1)):
                V = individual1.gene[pos]
                pos = individual2.gene.index(V)
            #find the position that isn't part of the swath, insert V to pos
            new_gene[pos] = tmp
    # copy any remaining positions from parent 2 to the child
    for i in range(0, individual1.gene_len):
        if new_gene[i] == -1:
            new_gene[i] = individual2.gene[i]

    return Individual(new_gene)


def Cy_cle_Crossover(individual1, individual2):
    #The Cycle Crossover operator identifies a number of so-called cycles between two parent chromosomes.
    # Then, to form Child, cycle one is copied from parent 1,
    # cycle 2 from parent 2, cycle 3 from parent 1, and so on.

    cont = 0
    new_gene = []
    # if value of a position in flag_list = 0,
    # drop down the value of the same position in parent 1
    # else parent 2.
    flag_list = [-1] * individual1.gene_len
    flag = 0
    while(cont < individual1.gene_len):
        if flag_list[cont] == -1:
        # find the loop
            begin = individual1.gene[cont]
            tmp2 = individual2.gene[cont]
            while(tmp2 != begin):
                loc = individual1.gene.index(tmp2)
                tmp2 = individual2.gene[loc]
                flag_list[loc] = flag
            flag_list[cont] = flag
            flag = 1 - flag # flip the flag
        cont += 1

    #drop down
    for i in range(0,individual1.gene_len):
        if flag_list[i] == 0:
            new_gene.append(individual1.gene[i])
        else:
            new_gene.append(individual2.gene[i])

    return Individual(new_gene)

def Edge_Recombination(individual1, individual2):
    new_gene = []
    cont = 0
    #generate neighbor list
    dic = dict()
    # initialize list
    for g in individual1.gene:
        s = set()
        dic[g] = s
    leng = individual1.gene_len
    for i in range(1, leng):
        dic[individual1.gene[i]].add(individual1.gene[i-1])
        dic[individual1.gene[i-1]].add(individual1.gene[i])
        dic[individual2.gene[i]].add(individual2.gene[i - 1])
        dic[individual2.gene[i - 1]].add(individual2.gene[i])

    # X is the first node from a random parent.
    if random.randint(0, 1) == 1:
        X = individual1.gene[0]
    else:
        X = individual2.gene[0]
    while (cont < individual1.gene_len):
        cont += 1
        new_gene.append(X)
        #remove all X
        Z = -1
        min = 100000
        minidx = -1
        for i in dic[X]:
            dic[i].discard(X)
            if(len(dic[i]) < min):
                min = len(dic[i])
                minidx = i
        # if X's neighbor list is empty, choose random node
        if len(dic[X]) == 0:
            for g in individual1.gene:
                if g not in new_gene:
                    Z = g
        else:
            # Determine neighbor of X that has fewest neighbors
            Z = minidx
        dic.pop(X)
        X = Z
    return Individual(new_gene)
