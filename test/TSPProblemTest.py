#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-22 00:56:48
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : $Id$

from EAlib.basic.TSPProblem import TSPProblem


def TSPProblemTest():
    node_coords = {
        1: (1, 1),
        2: (1, 0),
        3: (2, 2),
        4: (2, 0)
    }
    tsp = TSPProblem(mode=1, node_coordinates=node_coords)
    print(tsp.DM)

TSPProblemTest()
