#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-24 15:45:34
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : $Id$

import json
import argparse
import numpy as np
import matplotlib.pyplot as plt

from visual import load_result, get_pairs, load_tsp

def main(filename):
    """
    :param filename: the tsp output file name
    """
    tsp_problem = filename.split(".")[0]
    result = load_result(filename, "../output/result/output")
    return result, tsp_problem
    # tsp = "../tsp/%s.tsp" % result["tsp"]
    # info, node_coords = load_tsp(tsp)

    # best_one = result["result"]
    # plt.figure(f'{result["tsp"]}')
    # plt.title("{} fitness={:.2f}".format(tsp_problem, best_one['fitness']))
    # x, y = get_pairs(best_one["gene"], node_coords)
    # for i in range(len(x)):
    #     plt.plot(x[i], y[i], color='b')
    #     plt.scatter(x[i], y[i], color='r')

    # plt.savefig("../output/figure/%s.png" % tsp_problem)

if __name__ == '__main__':
    with open("../output/result/best_instance.json", "r") as f:
        data = json.load(f)
    result = {}
    for key, value in data.items():
        res, tsp = main(value[:-5])
        result[tsp] = res

    with open("best_algorithm.json", "w") as f:
        json.dump(result, f)