#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 21:02:25
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : 1.0

import re
import numpy as np

class TSPProblem(object):
    """docstring for TSPPrblem"""

    def __init__(self, mode, node_coordinates=None, dataloader=None):
        """
        :param mode: input node coordinates or dataloader, 1 or 2
        """
        super(TSPProblem, self).__init__()

        if mode == 1 and node_coordinates:
            self.node_coordinates = node_coordinates
        elif mode == 2 and dataloader:
            self.info, self.node_coordinates = dataloader.load()
        else:
            raise NotImplementedError(
                "mode = %d hasn't been implemented" % mode)

        self._compute()

    def _compute(self):
        """get distance matrix"""
        print("Begin computing distance matrix")
        # 2D, distance(i, j) = self.DM[i][j]
        N = len(self.node_coordinates)
        self.size = N
        # TODO: begin from 1 or 0???
        self.DM = np.zeros((N, N))

        # compute distance
        for i in range(N):
            for j in range(i, N):
                d = self._get_distance(self.node_coordinates[
                                       i + 1], self.node_coordinates[j + 1])
                self.DM[i][j] = d
                self.DM[j][i] = d

        print("Ending computing distance matrix")

    def _get_distance(self, coord1, coord2):
        """Get the distance of two node
        TODO: geography or not? ball or plane?
        """
        return np.linalg.norm(np.array(coord1) - np.array(coord2))