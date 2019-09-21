#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-22 00:00:53
# @Author  : Kaiyan Zhang (kyzhang@ir.hit.edu.cn)
# @Link    : https://github.com/iseesaw
# @Version : 1.0

import re

class BasicLoader(object):
    """
    +++++
    +++++ (information, like key : value)
    +++++ 
    NODE_COORD_SECTION
    idx x y
    ...
    """

    def __init__(self, filename):
        super(BasicLoader, self).__init__()

        self.filename = filename

    def load(self):
        """read cities information from the file"""

        # information of this tsp problem
        info = {}
        # nodes' coordinates
        node_coords = {}

        with open(self.filename, "r") as f:
            try:
                # record the beginning of the node coordinates
                flag = False
                for idx, line in enumerate(f.readlines()):
                    line = line.strip()

                    # end of the file
                    if line == "EOF" or line == "":
                        break

                    # flag the node coordinates
                    elif line == "NODE_COORD_SECTION":
                        flag = True
                        continue

                    # node coordinates
                    elif flag:
                        # the number of split space is  uncertain
                        items = re.split(r"\s+", line)
                        assert len(items) == 3, "Node Coordinate Must Like: index x y"
                        node_coords[int(items[0])] = (
                            float(items[1]), float(items[2]))

                    # information at the begining of the file
                    else:
                        items = line.replace(" ", "").split(":")
                        info[items[0]] = items[1]

            except:
                print("Failed to load %s" % self.filename)
                print("Line %d: %s" % (idx, line))
                return

        print("Load TSP Problem %s Successfully!" % self.filename)
        #print(info)

        return info, node_coords
