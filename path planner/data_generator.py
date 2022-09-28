from math import sqrt
from itertools import count
import random
import pandas as pd

from numpy import append

masukan = int(input("Masukan : "))

node = []
pos_x = []
pos_y = []

node_full = []

print("No Label X Y")
node_full.append(["No", "Label", "X", "Y"])

for i in range(masukan):
    n = "N" + str(i+1)
    x, y = random.randint(1, 20)*5, random.randint(1, 20)*5
    node.append(n)
    pos_x.append(x)
    pos_y.append(y)
    print(n + "  " + str(x) + "  " + str(y))
    node_full.append([i+1, n, x, y])

num_hub = []

df = pd.DataFrame(node_full)
writer = pd.ExcelWriter('Node.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False, header=False)
writer.save()


def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

# Locate the most similar neighbors


neighbors_distance = list()


def get_neighbors(train, test_row, num_neighbors):
    # a = 0
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        # print(dist)
        # print(train_row)
        distances.append((train_row, dist))
        # a += 1
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    # print(a)
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
        # neighbors_distance.append(distances[i][1])
    return neighbors


def get_neighbors_distance(train, test_row, num_neighbors):
    # a = 0
    distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        # print(dist)
        # print(train_row)
        # if a > 0:
        distances.append((train_row, dist))
        # a += 1
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    # print(a)
    for i in range(num_neighbors):
        # neighbors.append(distances[i][0])
        neighbors.append(distances[i][1])
    return neighbors


hubungan = []

for i in range(masukan):
    hubungan.append([pos_x[i], pos_y[i]])

# Test distance function

neighbors = []
dataset = hubungan

# print(hubungan)

for i in range(masukan):
    hub = random.randint(3, 5)
    num_hub.append(hub)
    neighbors.append(get_neighbors(dataset, dataset[i], hub))
    neighbors_distance.append(get_neighbors_distance(dataset, dataset[i], hub))


# [[0 for i in range(masukan)] for j in range(masukan)]
tetangga = [[] for i in range(masukan)]

c = 0

for neighbor in neighbors:
    for x in neighbor:
        for i in range(masukan):
            # for j in range(masukan):
            if(hubungan[i] == x):
                tetangga[c].append(i)  # tetangga[i][j] = 1
            else:
                pass
                # tetangga[i][j] = 0

    print(neighbor)
    c = c + 1
    # print(hubungan[0])

# print(tetangga)

mat_tetangga = [[0 for i in range(masukan)] for j in range(masukan)]
count_k = 0
# count_l = 0

for i in range(masukan):
    for k in tetangga[i]:
        for j in range(masukan):
            if(j == k):
                mat_tetangga[i][j] = 1

tetangga_full = []
t = [""] + node
tetangga_full.append(t)
# tetangga_full.extend(node)
for i in range(masukan):
    n = "N" + str(i+1)
    t = [n] + mat_tetangga[i]
    tetangga_full.append(t)
    # tetangga_full.extend(mat_tetangga[i])
    print(mat_tetangga[i])

# print(neighbors_distance)

# new_list = [["first", "second"], ["third", "four"], ["five", "six"]]
df = pd.DataFrame(tetangga_full)
writer = pd.ExcelWriter('Tetangga.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False, header=False)
writer.save()

mat_jarak = mat_tetangga

for i in range(masukan):
    for j in range(masukan):
        if i == j:
            mat_jarak[i][j] = 0

print()

for i in range(masukan):
    print(mat_jarak[i])

print()

k = 1
for i in range(masukan):
    for j in range(masukan):
        # print(k)
        if mat_jarak[i][j] == 1:
            # print("k = ")
            # print(k)
            # print("n = ")
            # print(len(neighbors_distance[i]))
            mat_jarak[i][j] = neighbors_distance[i][k]
            if k == len(neighbors_distance[i]):
                pass
            else:
                k += 1
            # print(k)
    k = 1

bobot_full = []
t = [""] + node
bobot_full.append(t)
# bobot_full.extend(node)
for i in range(masukan):
    t = list()
    n = "N" + str(i+1)
    t = [n] + mat_jarak[i]
    bobot_full.append(t)
    # bobot_full.extend(mat_jarak[i])
    # print(mat_jarak[i])

# print(bobot_full)

# new_list = [["first", "second"], ["third", "four"], ["five", "six"]]
df = pd.DataFrame(bobot_full)
writer = pd.ExcelWriter('Bobot.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False, header=False)
writer.save()
