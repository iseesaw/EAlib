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
from ..log import get_logger


class Naive_Ea(object):
    """docstring for Naive_Ea"""

    def __init__(self,
                 filename,
                 selection_func,
                 crossover_func,
                 mutation_func,
                 elitism=True,
                 unit_num=50,
                 max_gen=100,
                 prob_c=0.5,
                 prob_m=0.3,
                 print_every=50,
                 output_dir="output"):
        super(Naive_Ea, self).__init__()

        logger = get_logger()

        self.tsp = TSPProblem(mode=2, dataloader=BasicLoader(filename))

        logger.info(f"Run {filename}")
        logger.info(f"Selection: {selection_func.__name__}")
        logger.info(f"Crossover: {crossover_func.__name__}")
        logger.info(f"Mutation: {mutation_func.__name__}")

        self.population = Population(self.tsp,
                                     selection_func,
                                     crossover_func,
                                     mutation_func,
                                     elitism,
                                     unit_num,
                                     max_gen,
                                     prob_c,
                                     prob_m)
        self.population.evolve(print_every)

        filename = filename.split(
            "/")[-1] if "/" in filename else filename.split("\\")[-1]

        #self._for_grid(filename, output_dir, self.population)
        date = datetime.datetime.now()
        endfix = f"{date.year}-{date.month}-{date.day}.{date.hour}-{date.minute}"
        filename = f"{filename}.{selection_func.__name__.split('_')[0]}.{crossover_func.__name__.split('_')[0]}.{mutation_func.__name__.split('_')[0]}.{unit_num}.{max_gen}.{endfix}.json"

        logger.info("Save results to %s" % output_dir)
        self.save(filename, output_dir, self.population, max_gen)
        logger.info("That' all.")

    def save(self, filename, output_dir, population, max_gen):
        """Output to file"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(os.path.join(output_dir, filename), "w") as f:
            best_ones = {idx: {"fitness": individual.fitness, "gene": individual.gene}
                         for idx, individual in enumerate(population.best_ones)}
            save_best_ones = {idx:best_ones[idx] for idx in range(0, max_gen, 100)}
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
                "best_ones": save_best_ones
            }
            json.dump(record, f, indent=4)

    def _for_grid(self, filename, output_dir, population):
        with open("output/%s" % filename, "a") as f:
            f.write(f"{population.selection_func.__name__}\t{population.crossover_func.__name__}\t{population.mutation_func.__name__}\t{population.best_ones[-1].fitness}\n")


if __name__ == '__main__':
    Naive_Ea("tsp/att48.tsp")
