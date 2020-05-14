#!/usr/bin/env python3

import reader
import basic
import plot_util
import sys
import random
import min_ctor

if __name__ == "__main__":
    problem_name = 'xqf131'
    xy = reader.read_xy("problems/{}.tsp".format(problem_name))
    tour = min_ctor.make_tour(xy)
    plot_util.plot_tour(xy, tour)
