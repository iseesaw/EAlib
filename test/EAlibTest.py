#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-22 09:23:30
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : $Id$

import argparse

from EAlib.ea import Naive_Ea

from EAlib.operators.crossover import basic_crossover, Order_Crossover, Cy_cle_Crossover, Edge_Recombination, PMX_Crossover
from EAlib.operators.mutation import basic_mutation, insert_mutation, scramble_mutation, inversion_mutation, \
    swap_mutation
from EAlib.operators.selection import tournament_selection, fitnetss_proporitional, basic_selection, rank_based


def run(argv):
    selections = {
        "basic": basic_selection,
        "rank": rank_based,
        "tournament": tournament_selection,
        "fitnetss": fitnetss_proporitional
    }

    mutations = {
        "basic": basic_mutation,
        "insert": insert_mutation,
        "scramble": scramble_mutation,
        "inversion": inversion_mutation,
        "swap": swap_mutation
    }

    crossovers = {
        "basic": basic_crossover,
        "order": Order_Crossover,
        "cycle": Cy_cle_Crossover,
        "edge": Edge_Recombination,
        "pmx": PMX_Crossover
    }

    Naive_Ea(argv.filename,
             selections[argv.selection],
             crossovers[argv.crossover],
             mutations[argv.mutation],
             elitism=argv.elitism,
             unit_num=argv.unit_num,
             max_gen=argv.max_gen,
             prob_c=argv.prob_c,
             prob_m=argv.prob_m,
             print_every=argv.print_every,
             output_dir=argv.output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A Example to Using EAlib.")

    parser.add_argument("-filename", default="tsp/att48.tsp", help="TSP Problem file name")

    # function selction
    parser.add_argument("--selection", default="basic", help="selection function")
    parser.add_argument("--crossover", default="basic", help="crossover function")
    parser.add_argument("--mutation", default="basic", help="mutation function")
    parser.add_argument("--elitism", type=bool, default=True, help="elitism or not in the selection")

    # basic setting
    parser.add_argument("--unit_num", type=int, default=50, help="unit num of population")
    parser.add_argument("--max_gen", type=int, default=100, help="max generations")

    # more setting
    parser.add_argument("--prob_c", type=int, default=0.5, help="probability of crossover")
    parser.add_argument("--prob_m", type=float, default=0.3, help="probability of mutation")

    # others
    parser.add_argument("--print_every", type=int, default=1000, help="how many generations to print")

    parser.add_argument("--output_dir", type=str, default="output", help="output directionary")

    argv = parser.parse_args()

    print(f"\n{argv}\n")

    run(argv)
