#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-22 00:54:06
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : $Id$

import os
from EAlib.utils.dataloader import BasicLoader

def BasicLoaderTest():
    import os
    dirpath = "D:\\ACourse\\2019Fall\\EvolutionaryComputation\\TSP\\tsp"
    for file in os.listdir(dirpath):
        if file[-4:] == ".tsp":
            BasicLoader(os.path.join(dirpath, file)).load()

BasicLoaderTest()