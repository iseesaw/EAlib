#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-25 12:16:52
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : $Id$

import os
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt

from EAlib.utils.dataloader import BasicLoader


def main(argv):
    filename, tsp = argv.filename, argv.tsp
    result = load_result(filename)
    if not tsp:
        tsp = "tsp/%s.tsp" % result["tsp"]

    info, node_coords = load_tsp(tsp)

    print(f"{tsp} Information")
    print(info)
    print(f"\n{result['tsp']} Result")
    print(f"Training At {result['date']}")
    print(f"\nParameters:")
    print(f"{result['parameters']}")
    print(f"{result['result']['fitness']}\n")

    best_ones = result["best_ones"]

    plt.figure(f'{result["tsp"]}')
    for idx, best_one in enumerate(best_ones):
        # 刷新画板
        plt.clf()
        plt.title("{}th fitness={:.2f}".format(200*(idx+1), best_ones[str(best_one)]['fitness']))
        x, y = get_pairs(best_ones[str(best_one)]["gene"], node_coords)
        for i in range(len(x)):
            plt.plot(x[i], y[i], color='b')
            plt.scatter(x[i], y[i], color='r')
 
        plt.pause(argv.pause)

    plt.show()

def get_pairs(gene, node_coords):
    gene.append(gene[0])
    x, y = [], []
    for idx, node in enumerate(gene[:-1]):
        next_node = gene[idx + 1]

        coord = node_coords[node + 1]
        coord_next = node_coords[next_node + 1]
        x.append([coord[0], coord_next[0]])
        y.append([coord[1], coord_next[1]])
    return x, y


def load_result(filename, filedir="output"):
    if not filename:
        raise FileNotFoundError(f"Result file {filename} is not found.")

    with open(os.path.join(filedir, "%s.json" % filename), "r", encoding="utf-8") as f:
        result = json.load(f)
    return result


def load_tsp(tsp):
    if not tsp:
        raise FileNotFoundError(f"TSP problem file {tsp} is not found.")

    loader = BasicLoader(tsp)
    info, node_coords = loader.load()
    return info, node_coords

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="TSP Problem Result Visualization.")
    parser.add_argument("-filename", default=None, help="output result file name")
    parser.add_argument("--tsp", default=None, help="tsp problem file")
    parser.add_argument("--pause", type=float, default=0.5, help="time to pause")

    argv = parser.parse_args()
    print(argv)
    main(argv)