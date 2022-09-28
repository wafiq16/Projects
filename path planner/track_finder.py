# BFS algorithm in Python

import collections
from itertools import combinations

# BFS algorithm


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


# DFS algorithm in Python
# DFS algorithm
num_step = []
step = []
finish = False


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def get_number(input):
    node = list()
    c = 0
    for i in input:
        c += 1
        if i == 1:
            node.append(c)
    return node


def get_price(path, bobot, dim=10):
    price = 0
    step = len(path)-2
    # print(step)
    # print(bobot)
    for i in range(step):
        price += bobot[path[i]-1][path[i+1]-1]
        # print(bobot[path[i]-1][path[i+1]-1])
        # print(path[i])
        # print(path[i+1])
    # print(list(comb))
    # for i in path:
    # price = bobot[i][len(path)-1-i]
    # print(i)
    # print(price)
    return price


if __name__ == '__main__':
    import pandas as pd

    # can also index sheet by name or fetch all sheets
    df = pd.read_excel('Tetangga.xlsx')
    n_1 = df['N1'].tolist()
    n_2 = df['N2'].tolist()
    n_3 = df['N3'].tolist()
    n_4 = df['N4'].tolist()
    n_5 = df['N5'].tolist()
    n_6 = df['N6'].tolist()
    n_7 = df['N7'].tolist()
    n_8 = df['N8'].tolist()
    n_9 = df['N9'].tolist()
    n_10 = df['N10'].tolist()

    node_1 = get_number(n_1)
    node_2 = get_number(n_2)
    node_3 = get_number(n_3)
    node_4 = get_number(n_4)
    node_5 = get_number(n_5)
    node_6 = get_number(n_6)
    node_7 = get_number(n_7)
    node_8 = get_number(n_8)
    node_9 = get_number(n_9)
    node_10 = get_number(n_10)
    graph_d = {1: set(node_1), 2: set(node_2), 3: set(node_3), 4: set(node_4), 5: set(
        node_5), 6: set(node_6), 7: set(node_7), 8: set(node_8), 9: set(node_9), 10: set(node_10)}

    df_b = pd.read_excel('Bobot.xlsx')
    n_1 = df_b['N1'].tolist()
    n_2 = df_b['N2'].tolist()
    n_3 = df_b['N3'].tolist()
    n_4 = df_b['N4'].tolist()
    n_5 = df_b['N5'].tolist()
    n_6 = df_b['N6'].tolist()
    n_7 = df_b['N7'].tolist()
    n_8 = df_b['N8'].tolist()
    n_9 = df_b['N9'].tolist()
    n_10 = df_b['N10'].tolist()

    # print(n_1)

    bobot_1 = n_1
    bobot_2 = n_2
    bobot_3 = n_3
    bobot_4 = n_4
    bobot_5 = n_5
    bobot_6 = n_6
    bobot_7 = n_7
    bobot_8 = n_8
    bobot_9 = n_9
    bobot_10 = n_10

    bobot = []
    bobot.append(bobot_1)
    bobot.append(bobot_2)
    bobot.append(bobot_3)
    bobot.append(bobot_4)
    bobot.append(bobot_5)
    bobot.append(bobot_6)
    bobot.append(bobot_7)
    bobot.append(bobot_8)
    bobot.append(bobot_9)
    bobot.append(bobot_10)

    # print(bobot)
    # graph_b = {1: node_1, 2: node_2, 3: node_3, 4: node_4, 5: node_5,
    #            6: node_6, 7: node_7, 8: node_8, 9: node_9, 10: node_10}

    x, y, z = input("Input: ").split(",")

    # print(type(x))

    awal = int(x[1:])
    akhir = int(y[1:])
    # print(awal)
    # dfs(graph_d, 5)
    if z == "BFS":
        print(list(bfs_paths(graph_d, awal, akhir))[0])
        print(get_price(list(bfs_paths(graph_d, awal, akhir))[0], bobot))
    elif z == "DFS":
        print(list(dfs_paths(graph_d, awal, akhir))[0])
        print(get_price(list(dfs_paths(graph_d, awal, akhir))[0], bobot))
    # bfs(graph_d, 5)
    # print(get_price(list(dfs_paths(graph_d, 2, 10))[0], bobot))

# bfs(graph, 0)
