#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:08:09
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : 1.0

import os
import json
import datetime

from ..basic import Individual, Population, TSPProblem
from ..utils import BasicLoader
from ..operators.mutation import basic_mutation
from ..operators.crossover import basic_crossover
from ..operators.selection import basic_selection
from ..log import get_logger

class Naive_Ea(object):
    """docstring for Naive_Ea"""

    def __init__(self,
                 filename,
                 selection_func=basic_selection,
                 crossover_func=basic_crossover,
                 mutation_func=basic_mutation,
                 unit_num=50,
                 max_gen=100,
                 prob_c=0.5,
                 prob_m=0.3,
                 print_every=50,
                 output_dir="output"):
        super(Naive_Ea, self).__init__()

        logger = get_logger()

        self.tsp = TSPProblem(mode=2, dataloader=BasicLoader(filename))

        logger.info(f"Selection: {selection_func.__name__}")
        logger.info(f"Crossover: {crossover_func.__name__}")
        logger.info(f"Mutation: {mutation_func.__name__}")

        self.population = Population(self.tsp,
                                     basic_selection,
                                     basic_crossover,
                                     basic_mutation,
                                     unit_num,
                                     max_gen,
                                     prob_c,
                                     prob_m)
        self.population.evolve(print_every)

        logger.info("Save results to %s" % output_dir)
        self.save(filename, output_dir, self.population)
        logger.info("That' all.")

    def save(self, filename, output_dir, population):
        """Output to file"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = filename.split("/")[-1] if "/" in filename else filename.split("\\")[-1] 
        with open(os.path.join(output_dir, "%s.json" % filename), "w") as f:
            best_ones = {idx: {"fitness": individual.fitness, "gene": individual.gene}
                         for idx, individual in enumerate(population.best_ones)}
            record = {
                "tsp": filename.split(".")[0],
                "date": str(datetime.datetime.now()),
                "parameters": {
                    "selection": population.selection_func.__name__,
                    "crossover": population.crossover_func.__name__,
                    "mutation": population.mutation_func.__name__,
                    "unit_num": population.unit_num,
                    "max_gen": population.max_gen,
                    "prob_c": population.prob_c,
                    "prob_m": population.prob_m
                },
                "result": {
                    "fitness": population.best_ones[-1].fitness,
                    "gene": population.best_ones[-1].gene
                },
                "best_ones": best_ones
            }
            json.dump(record, f, indent=4)


if __name__ == '__main__':
    Naive_Ea("tsp/att48.tsp")
