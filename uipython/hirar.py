# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:20:51 2021

@author: Denise
"""

import time
import pandas as pd
import numpy as np

import kmeans as m
from sklearn.decomposition import PCA


class Hierarchical:
    def __init__(self, datapoints: np.array, label, indexes, child: tuple = None, distance=0):
        self.datapoints = datapoints
        self.label = label
        self.distance = distance
        self.indexes = indexes
        self.child = child

    @staticmethod
    def castObject(obj: 'Hierarchical'):
        return obj


def flatten(*n):
    return (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))


class Clusters:
    def __init__(self, data: pd.DataFrame):
        label = data.values[:, [0]].flatten()
        values = data.values[:, 1:]
        pca = PCA(n_components=3)
        values = pca.fit_transform(values)
        values = pd.DataFrame(values)
        # values.columns = ['P1', 'P2', 'P3']
        values = values.values[:, :]
        N = len(values)
        self.clusters = np.array(
            [Hierarchical(values[i], label[i], [i]) for i in range(N)])
        self.distance = m.eucledian

    @staticmethod
    def joinClusters(cluster1: Hierarchical, cluster2: Hierarchical, distance):
        return Hierarchical((
            cluster1.datapoints+cluster2.datapoints)/2,
            [list(flatten(cluster1.label)), list(flatten(cluster2.label))],
            cluster1.indexes + cluster2.indexes,
            (cluster1, cluster2),
            distance
        )

    @staticmethod
    def splitClusters(cluster: Hierarchical, k):
        result = [cluster]

        curr = k
        while curr > 1:
            find = [item for item in result if item.distance > 0]
            item = find[0]
            result.remove(item)
            result += list(item.child)
            curr -= 1
        return list(result)

    def run(self):
        if len(self.clusters) < 1:
            return
        tempClusters = []

        print(f'First scan: {len(self.clusters)}')

        start_time = time.time()
        Clusters.joinClusters(
            self.clusters[0], self.clusters[1],
            self.distance(self.clusters[0].datapoints,
                          self.clusters[1].datapoints)
        )
        end_time = time.time() - start_time
        N = len(self.clusters)
        print(f'Estimated done in {end_time*N*(N+1)/2} s')
        tempClusters = np.array([
            Clusters.joinClusters(
                self.clusters[i],
                self.clusters[j],
                self.distance(
                    self.clusters[i].datapoints, self.clusters[j].datapoints)
            ) for i in range(N-1) for j in range(i+1, N)
        ])
        start_time = time.time()
        while len(self.clusters) > 2:
            print('Len of cluster: ' + str(len(self.clusters)))
            distances = [item.distance for item in tempClusters]
            smallest = tempClusters[distances.index(min(distances))]
            smallest = Hierarchical.castObject(smallest)

            for child in smallest.child:
                self.clusters = np.delete(
                    self.clusters, np.where(self.clusters == child))
                tempClusters = np.delete(
                    tempClusters, [child in item.child for item in tempClusters])
            self.clusters = np.append(self.clusters, smallest)
            new_joins = np.array([
                Clusters.joinClusters(smallest, item, self.distance(
                    smallest.datapoints, item.datapoints))
                for item in self.clusters[:-1]])
            tempClusters = np.concatenate((tempClusters, new_joins))
            # return tempClusters
        print(f'Took {time.time()-start_time}s')


# data = pd.read_csv('bahan.csv')

# label = data.values[:, [0]].flatten()
# values = data.values[:,1:]
# start_time = time.time()
# pca = PCA(n_components=3)
# values = pca.fit_transform(values)
# values = pd.DataFrame(values)
# values.columns = ['P1', 'P2', 'P3']

# values_sum = np.sum(values, axis=0)/len(values)
# # print(data.head())
# clusts = Clusters(data)
# clusts.run()
# print(f'Took {time.time()-start_time}s')
# clusters = Hierarchical.castObject(clusts.clusters[0])
# # for i in range(1, len(values)):
# #   j = 0
# #   print(f'Splitting cluster into {i}')
# #   for item in Clusters.splitClusters(clusters, i):
# #     j+=1
# #     print(f'Cluster {j}: Range = {np.sqrt(m.eucledian(values_sum, item.datapoints))}')
# #     print(item.label)
#   # print(item.label,  file=open("outputHirar_test.txt", "a"))

# n_cluster=5
# j=0
# for item in Clusters.splitClusters(clusters, n_cluster):
#   # lines=['Cluster {j+1} : \n {item.label}']
#   # print(lines)
#   # print(item.label)
#   with open('hasil2.txt', 'a') as f:
#     f.writelines('Cluster {} \n {} \n'.format(j, item.label))
#   j +=1
