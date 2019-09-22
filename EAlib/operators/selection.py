#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:04:59
# @Author  :
# @Link    :
# @Version : 1.0s

import random

def basic_selection(population):
    """
    :param population: Population Object
    :return: Individual Obejct
    """
    return random.choice(population.individuals)


def fitnetss_proporitional(population):
    """TODO"""
    raise NotImplementedError


def tournament_selection(population):
    """TODO"""
    raise NotImplementedError


def elitism(population):
    """TODO"""
    raise NotImplementedError
