#!/usr/bin/env python3

import basic
import random

def get_all_edges(xy):
    """Gets all (n-1)*(n)/2 edges. Returns list of tuples : (cost, (i, j))
    i, j are the point IDs in the edge, in no particular order.
    """
    edges = []
    n = len(xy)
    for i in range(n-1):
        for j in range(i + 1, n):
            if i == j:
                continue
            edge = [i, j]
            random.shuffle(edge)
            edges.append((basic.distance(xy, i, j), edge))
    return edges

def make_edges(xy):
    edges = get_all_edges(xy)
    edges.sort()
    done = set() # points that have degree 2 and can no longer accept edges.
    segments = {} # maps lowest-valued endpoint to segment.
    for edge in edges:
        e = edge[1]
        if e[0] in done or e[1] in done:
            continue
        if e[0] not in segments and e[1] not in segments:
            # create new segment from edge.
            segment = {'summary': e, 'edges': [e]}
            segments[min(e)] = segment
            segments[max(e)] = segment
        elif e[0] in segments and e[1] in segments:
            # edge bridges 2 segments.
            s = segments[min(e)]
            other = segments[max(e)]
            # check if this creates a cycle, and only allow if last edge in the tour.
            if s['summary'] == other['summary']:
                if len(done) == len(xy) - 2:
                    assert(len(s['edges']) == len(xy) - 1)
                    return s['edges'] + [e]
                continue # skip; don't want to close loop yet.
            s['edges'] += other['edges'] + [e]
            s['summary'] = list(s['summary']) + list(other['summary'])
            s['summary'] = [x for x in s['summary'] if x not in e]
            assert(len(s['summary']) == 2)
            del segments[min(e)]
            del segments[max(e)]
            done.add(min(e))
            done.add(max(e))
            segments[s['summary'][0]] = s
            segments[s['summary'][1]] = s
        elif e[0] in segments:
            s = segments[e[0]]
            s['edges'].append(e)
            new_end = s['summary'][0]
            if new_end in e:
                new_end = s['summary'][1]
            s['summary'] = (new_end, e[1])
            del segments[e[0]]
            done.add(e[0])
            segments[e[1]] = s
        elif e[1] in segments:
            s = segments[e[1]]
            s['edges'].append(e)
            new_end = s['summary'][0]
            if new_end in e:
                new_end = s['summary'][1]
            s['summary'] = (new_end, e[0])
            del segments[e[1]]
            done.add(e[1])
            segments[e[0]] = s
        else:
            assert(False)
    assert(False)

def make_adjacency_map(edges):
    adjacency = {}
    for e in edges:
        if e[0] not in adjacency:
            adjacency[e[0]] = []
        if e[1] not in adjacency:
            adjacency[e[1]] = []
        adjacency[e[0]].append(e[1])
        adjacency[e[1]].append(e[0])
    for i in adjacency:
        assert(len(adjacency[i]) == 2)
    return adjacency

def walk_adjacency_map(adjacency_map):
    start = 0
    i = adjacency_map[start][0]
    prev = start
    tour = []
    while i != start:
        tour.append(i)
        if adjacency_map[i][0] == prev:
            prev = i
            i = adjacency_map[i][1]
        else:
            prev = i
            i = adjacency_map[i][0]
    tour.append(i)
    return tour

def make_tour(xy):
    edges = make_edges(xy)
    adj = make_adjacency_map(edges)
    return walk_adjacency_map(adj)

