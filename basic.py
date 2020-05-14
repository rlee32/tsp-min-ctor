#!/usr/bin/env python3

def distance_to_next(xy, i):
    j = (i + 1) % len(xy)
    dx = xy[i][0] - xy[j][0]
    dy = xy[i][1] - xy[j][1]
    return round((dx ** 2 + dy ** 2) ** 0.5)

def distance(xy, i, j):
    dx = xy[i][0] - xy[j][0]
    dy = xy[i][1] - xy[j][1]
    return round((dx ** 2 + dy ** 2) ** 0.5)

def edge_cost(xy, edge):
    return distance(xy, edge[0], edge[1])
def edge_cost_sum(xy, edges):
    total = 0
    for e in edges:
        total += edge_cost(xy, e)
    return total

def midpoint(xy, i, j):
    dx = xy[j][0] - xy[i][0]
    dy = xy[j][1] - xy[i][1]
    return (xy[i][0] + dx / 2.0, xy[i][1] + dy / 2.0)

def tour_length(xy, node_ids):
    assert(len(xy) > 1)
    assert(len(node_ids) > 1)
    seen = set()
    n = len(xy)
    L = 0
    prev = node_ids[-1]
    seen.add(prev)
    for i in node_ids:
        L += distance(xy, i, prev)
        prev = i
        seen.add(i)
    assert(len(seen) == len(node_ids))
    return L

def cyclic(nexts):
    n = len(nexts) - 1
    end = 0
    current = nexts[end]
    seen = set()
    seen.add(current)
    while current != end:
        current = nexts[current]
        if current in seen:
            return False
        seen.add(current)
    return n == 0 and len(seen) == len(nexts)

def edges_from_order(node_ids):
    edges = set()
    prev = node_ids[-1]
    for i in node_ids:
        edge = (min(i, prev), max(i, prev))
        edges.add(edge)
        prev = i
    return edges

def write_edges(edges, output_file_path):
    with open(output_file_path, "w") as f:
        for e in edges:
            e = [str(x) for x in e]
            f.write(" ".join(e) + "\n")
def write_edges_from_order(order, output_file_path):
    edges = edges_from_order(order)
    write_edges(edges, output_file_path)
def write_walk_edges(points, output_file_path):
    with open(output_file_path, "w") as f:
        for i in range(len(points) - 1):
            f.write(" ".join([str(points[i]), str(points[i + 1])]) + "\n")
