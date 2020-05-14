#!/usr/bin/env python3

# Works on tour representations that are simply sequences of node IDs in [0, problem_size).

import basic
import random

def default(xy):
    return [i for i in range(len(xy))]

def double_bridge(tour):
    """Applies a double bridge perturbation to the input tour."""
    n = len(tour)
    indices = []
    # indices for first non-sequential 2-opt move.
    i0 = random.randrange(n)
    indices.append(i0)
    j0 = random.randrange(3, n - 2) # relative to i0
    indices.append((i0 + j0) % n)
    # indices for second non-sequential 2-opt move.
    a0 = random.randrange(j0)
    indices.append((i0 + a0 + 1) % n)
    b0 = random.randrange(n - j0)
    indices.append((j0 + b0 + 1) % n)
    indices.sort()
    new_tour = tour[:indices[0]+1] + tour[indices[2]+1:indices[3]+1] + tour[indices[1]+1:indices[2]+1] + tour[indices[0]+1:indices[1]+1] + tour[indices[3]+1:]
    assert(len(new_tour) == n)
    return new_tour

def edges(tour):
    edges = set()
    prev = tour[-1]
    for i in tour:
        edge = (min(i, prev), max(i, prev))
        edges.add(edge)
        prev = i
    return edges

def factor(tour1, tour2):
    """Breaks the tours into edges, and returns a tuple of: common edges, edges only in tour1,
    and edges only in tour 2.
    """
    edges1 = edges(tour1)
    edges2 = edges(tour2)
    diff1 = set()
    common = set()
    for edge in edges1:
        if edge not in edges2:
            diff1.add(edge)
        else:
            common.add(edge)
    diff2 = set()
    for edge in edges2:
        if edge not in edges1:
            diff2.add(edge)
    assert(len(common) + len(diff1) == len(tour1))
    assert(len(diff1) == len(diff2))
    return common, diff1, diff2

def length(xy, tour):
    seen = set()
    n = len(tour)
    L = 0
    for i in range(n):
        L += basic.distance(xy, tour[i-1], tour[i])
        seen.add(tour[i])
    assert(len(seen) == len(tour))
    return L

