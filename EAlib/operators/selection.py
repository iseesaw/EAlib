#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:04:59
# @Author  : Runxin Sun (vercosun@gmail.com)
# @Link    : https://github.com/1160300911
# @Version : 1.0s

from itertools import accumulate
from bisect import bisect_right
import random

def basic_selection(population):
    """
    :param population: Population Object
    :return: Individual Obejct
    """
    return random.choice(population.individuals)


def fitnetss_proporitional(population):
    """
    :param population: Population Object
    :return: Individual Obejct
    """
    # Normalize fitness values for all individuals.
    fits = [(1 / population.get_disctance(indv)) for indv in population.individuals]
    min_fit = min(fits)
    fits = [(fit - min_fit) for fit in fits]

    # Create roulette wheel.
    sum_fit = sum(fits)
    wheel = list(accumulate([(fit / sum_fit) for fit in fits]))

    # Select an individual.
    idx = bisect_right(wheel, random.random())
    return population.individuals[idx]


def rank_based(population, pmin=0.1, pmax=0.9):
    """
    :param population: Population Object
    :param pmin: minimum probability of being selected
    :param pmax: maximum probability of being selected
    :return: Individual Obejct
    """
    # Initialize parameters.
    n = population.unit_num
    sorted_indvs = sorted(population.individuals, key=population.get_disctance, reverse=True)

    # Assign selection probabilities linearly.
    p = lambda i: pmin + (pmax - pmin) * (i - 1) / (n - 1)
    ps = [p(i) for i in range(1, n+1)]

    # Normalize probabilities.
    sum_p = sum(ps)
    wheel = list(accumulate([(p / sum_p) for p in ps]))

    # Select an individual.
    idx = bisect_right(wheel, random.random())
    return sorted_indvs[idx]


def tournament_selection(population, tournament_size=2):
    """
    :param population: Population Object
    :param tournament_size: number of individuals participating in the tournament (default is 2)
    :return: Individual Obejct
    """
    # Competition function.
    complete = lambda competitors: min(competitors, key=population.get_disctance)

    # Check validity of tournament size.
    if tournament_size > len(population.individuals):
        msg = 'tournament size({}) is larger than population size({})'
        raise ValueError(msg.format(tournament_size, len(population.individuals)))

    # Pick the winner of the group and return it.
    competitors = random.sample(population.individuals, tournament_size)
    return complete(competitors)
