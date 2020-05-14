#!/usr/bin/env python3

from matplotlib import pyplot as plt
import tour_util

def plot_tour(xy, tour):
    n = len(tour)
    x = [xy[i][0] for i in tour]
    y = [xy[i][1] for i in tour]
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, 'x:k')
    plt.show()

def plot_edges(xy, edges, color):
    for edge in edges:
        a = xy[edge[0]]
        b = xy[edge[1]]
        plt.plot([a[0], b[0]], [a[1], b[1]], ':x{}'.format(color))

def plot_difference(xy, tour1, tour2):
    common, edges1, edges2 = tour_util.factor(tour1, tour2)
    plot_edges(xy, common, 'k')
    plot_edges(xy, edges1, 'b')
    plot_edges(xy, edges2, 'r')
    plt.show()

