# CS 610 Spring 2023
# Instructor: Ravi Varadarajan
# Performance of Treaps Project
#Date: 2/MAY/2023


# !pip install treap #UNCOMMENT TO INSTALL TREAP IN YOUR MACHINE

from treap import Treap
from time import time
import matplotlib.pyplot as plt
import time
import random

# Import necessary variables


def test_performance():
    treap = Treap()
    n = 100000
    keys = list(range(1, n + 1))
    random.shuffle(keys)

    times = {'insert': [], 'find': [], 'remove': [], 'split': [], 'join': []}
    for i in range(n):
        key = keys[i]
        treap.insert(key)
        if i % 5 == 0:
            t0 = time()
            treap.find(key)
            times['find'].append(time() - t0)

            t0 = time()
            treap.remove(key)
            times['remove'].append(time() - t0)

            t0 = time()
            treap.split(key)
            times['split'].append(time() - t0)

            t0 = time()
            T = Treap()
            T.insert(key)
            treap.join(T)
            times['join'].append(time() - t0)

        if i % 10 == 0:
            t0 = time()
            treap.insert(random.randint(n + 1, 2 * n))
            times['insert'].append(time() - t0)

    return times


if __name__ == '__main__':
    results = []
    for i in range(5):
        results.append(test_performance())

    sizes = list(range(0, 100001, 10))
    averages = {'insert': [], 'find': [],
                'remove': [], 'split': [], 'join': []}
    for size in sizes:
        insert_times = []
        find_times = []
        remove_times = []
        split_times = []
        join_times = []
        for i in range(5):
            insert_times.append(sum(results[i]['insert'][:size]) / size)
            find_times.append(sum(results[i]['find'][:size]) / size)
            remove_times.append(sum(results[i]['remove'][:size]) / size)
            split_times.append(sum(results[i]['split'][:size]) / size)
            join_times.append(sum(results[i]['join'][:size]) / size)
        averages['insert'].append(sum(insert_times) / 5)
        averages['find'].append(sum(find_times) / 5)
        averages['remove'].append(sum(remove_times) / 5)
        averages['split'].append(sum(split_times) / 5)
        averages['join'].append(sum(join_times) / 5)
# Plots the diagram
    plt.plot(sizes, averages['insert'], label='Insert')
    plt.plot(sizes, averages['find'], label='Find')
    plt.plot(sizes, averages['remove'], label='Remove')
    plt.plot(sizes, averages['split'], label='Split')
    plt.plot(sizes, averages['join'], label='Join')
    plt.legend()
    plt.xlabel('Size of Treap')
    plt.ylabel('Time (seconds)')
    plt.show()
