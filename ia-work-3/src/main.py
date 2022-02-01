from pandas import read_csv
from math import sqrt
from typing import List

from centroid import Centroid
from iris import Iris, dict_iris

CentroidList = List[Centroid]

def distance(point: list, centroid: Centroid):
    _sum = 0
    for column in range(len(point)):
        _sum += (point[column] - centroid.position[column]) ** 2
    return sqrt(_sum)


def get_nearest_centroid(point: list, centroids: CentroidList):
    nearest = 0
    distanceNearest = distance(point, centroids[0])

    for i in range(1, len(centroids)):
        new_distance = distance(point, centroids[i])
        if(new_distance < distanceNearest):
            nearest = i
            distanceNearest = new_distance

    return nearest


def init_centroids(points: list, k: int) -> CentroidList:
    centroids = list()
    partition = int(len(points) / k)

    for i in range(k):
        new_centroid = Centroid(Iris(i), points[i * partition])
        centroids.append(new_centroid)
    return centroids


def read_file() -> list:
    data_file = read_csv('iris-dataset/iris.data', sep=',', header=None) 
    data_file.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class']

    values = data_file.values
    points = values[:, :4]
    classifications = values[:, 4]

    return [points, classifications]


def recalculate_centroid(centroid: Centroid, points: list, class_points: list):
    was_update = False

    for column in range(len(centroid.position)):
        sum = 0
        qtd_points_in_iris = 0

        for i in range(len(points)):
            if(class_points[i] == centroid.iris):
                sum += points[i][column]
                qtd_points_in_iris += 1

        if(qtd_points_in_iris > 0):
            if(centroid.position[column] != sum/qtd_points_in_iris):
                centroid.position[column] = sum/qtd_points_in_iris
                was_update = True
        else:
            if(centroid.position[column] != 0):
                centroid.position[column] = 0
                was_update = True

    return (was_update, centroid)


def hits(classifications: list, class_points: list):
    qtd_hits = 0

    for i in range(len(classifications)):
        if(classifications[i] == dict_iris.get(class_points[i])):
            qtd_hits += 1

    return qtd_hits


def main():
    number_clusters = 3 # (Iris Setosa, Iris Versicolour, Iris Virginica)
    centroids = CentroidList
    centroids_was_update = True

    [points, classifications] = read_file()
    centroids = init_centroids(points, number_clusters)
    class_points = [Iris.Setosa for _i in range(len(points))]

    while centroids_was_update:
        for i in range(len(points)):
            nearest_centroid = get_nearest_centroid(points[i], centroids)
            class_points[i] = centroids[nearest_centroid].iris

        for i in range(len(centroids)):
            (was_update, centroids[i]) = recalculate_centroid(centroids[i], points, class_points)
            centroids_was_update = centroids_was_update and was_update

    qtd_hits = hits(classifications, class_points)
    print('Quantidade de Acertos: %d' % qtd_hits)


if __name__ == "__main__":
    main()