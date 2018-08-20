import math
import matplotlib.pyplot as plt
from collections import Counter
import random


def bucketize(point, bucket_size):
    return bucket_size * math.floor(point/bucket_size)


def make_histogram(points, bucket_size):
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points, bucket_size, title=""):
    h = make_histogram(points, bucket_size)
    plt.bar(h.keys(), h.values(), width=bucket_size)
    plt.title(title)
    plt.show()

random.seed()

u = [200 * random.random() - 100 for _ in range(10000)]

plot_histogram(u, 10, "Uniform histogram")
