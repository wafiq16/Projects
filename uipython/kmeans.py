import numpy as np
import pandas as pd
# import pandas as pd
# import numpy as np
import random
import functools
import time


class KMeans():
    def __init__(self, data: pd.DataFrame, k):
        self.result = None
        self.data = data
        self.distance = cosine
        self.k = k
        self.iteration = 10

    @classmethod
    def euclidean(cls, data: pd.DataFrame, k=5):
        cluster = cls(data, k)
        cluster.distance = eucledian
        return cluster

    @classmethod
    def manhattan(cls, data: pd.DataFrame, k=5):
        cluster = cls(data, k)
        cluster.distance = manhattan
        return cluster

    @classmethod
    def cosine(cls, data: pd.DataFrame, k=5):
        cluster = cls(data, k)
        cluster.distance = cosine
        return cluster

    def run(self):

        Ny = self.data.shape[0]  # Data rows m
        Nx = self.data.shape[1]  # n data points

        Centroids = np.array([]).reshape(Nx, 0)

        for i in range(self.k):
            rand = random.randint(0, Ny-1)
            # Pick random points
            Centroids = np.c_[Centroids, self.data[rand]]

        clusters = {}
        clustersIdx = {}

        print('Start KMeans using k = ', self.k)
        print('Start KMeans using k = ', self.iteration)
        for i in range(self.iteration):
            print('Kmeans Iteration', ' ', i)
            Distance = np.array([]).reshape(Ny, 0)
            for k in range(self.k):
                print('Kmeans Iteration(distance) = ', ' ', k)
                tempDistance = []
                for item in self.data:
                    tempDistance.append(self.distance(item, Centroids[:, k]))
                Distance = np.c_[Distance, np.array(tempDistance)]

            C = np.argmin(Distance, axis=1)+1

            Y = {}
            I = {}
            for k in range(self.k):
                Y[k+1] = np.array([]).reshape(Nx, 0)
                I[k+1] = []
            for i in range(Ny):
                Y[C[i]] = np.c_[Y[C[i]], self.data[i]]
                I[C[i]].append(i)

            for k in range(self.k):
                Y[k+1] = Y[k+1].T

            for k in range(self.k):
                Centroids[:, k] = np.mean(Y[k+1], axis=0)
            clustersIdx = I

        self.result = clustersIdx


def pearson(v1, v2):
    n = len(v1)
    var_1 = np.array(v1)
    var_2 = np.array(v2)
    # Simple sums
    sum1 = np.sum(var_1)
    sum2 = np.sum(var_2)

    # Sums of the squares
    sum1Sq = np.sum(np.power(var_1, 2))
    sum2Sq = np.sum(np.power(var_2, 2))

    # Sum of the products
    pSum = np.sum(var_1*var_2)

    # Calculate r (Pearson score)
    num = pSum-(sum1*sum2/n)
    den = np.sqrt((sum1Sq-np.power(sum1, 2)/n)*(sum2Sq-np.power(sum2, 2)/n))
    if den == 0:
        return 0

    return 1.0-num/den


def eucledian(raw_p, raw_q):
    p = np.array(raw_p)
    q = np.array(raw_q)

    return np.sqrt(np.sum((p-q)**2))


def manhattan(raw_p, raw_q):
    x = np.array(raw_p)
    y = np.array(raw_q)

    return np.abs(x-y).sum()


def eucledian2(raw_p, raw_q):
    x = np.array(raw_p)
    y = np.array(raw_q)
    dist = np.sqrt(np.dot(x, x) - 2 * np.dot(x, y) + np.dot(y, y))
    return dist


def cosine(raw_p, raw_q):
    a = np.array(raw_p)
    b = np.array(raw_q)
    result = np.dot(a, b)/(np.norm(a)*np.norm(b))
    return result
