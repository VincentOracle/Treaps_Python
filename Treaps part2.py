
# !pip install treap #UNCOMMENT TO INSTALL TREAP IN YOUR MACHINE


import random
import time
from treap import Treap

# You can adjust the number of operations by changing the argument passed to
# test_performance. You should also run the script multiple times with different
# numbers of operations to get a good estimate of the average execution times.
# Finally, you can plot the average times as a function of the size of the treap to analyze the


def test_performance(n):
    treap = Treap()
    keys = set()

    for i in range(n):
        # Generate random key
        key = random.randint(1, 100000)
        while key in keys:
            key = random.randint(1, 100000)
        keys.add(key)

        # Insert key
        start_time = time.time()
        treap.insert(key)
        end_time = time.time()
        insert_time = end_time - start_time

        # Perform other operations with equal probability
        operation = random.choice(['find', 'remove', 'split', 'join'])
        start_time = time.time()
        if operation == 'find':
            treap.find(key)
        elif operation == 'remove':
            treap.remove(key)
        elif operation == 'split':
            treap.split(key)
        elif operation == 'join':
            t = Treap()
            for j in range(random.randint(1, 100)):
                t.insert(random.randint(1, 100000))
            treap.join(t)
        end_time = time.time()
        operation_time = end_time - start_time

        # Print time for debugging
        print(f"{i+1}\t{insert_time:.6f}\t{operation_time:.6f}")

    # Calculate average time for each operation
    insert_times = []
    find_times = []
    remove_times = []
    split_times = []
    join_times = []
    for i in range(n):
        key = random.randint(1, 100000)

        start_time = time.time()
        treap.insert(key)
        end_time = time.time()
        insert_times.append(end_time - start_time)

        start_time = time.time()
        treap.find(key)
        end_time = time.time()
        find_times.append(end_time - start_time)

        start_time = time.time()
        treap.remove(key)
        end_time = time.time()
        remove_times.append(end_time - start_time)

        start_time = time.time()
        treap.split(key)
        end_time = time.time()
        split_times.append(end_time - start_time)

        t = Treap()
        for j in range(random.randint(1, 100)):
            t.insert(random.randint(1, 100000))
        start_time = time.time()
        treap.join(t)
        end_time = time.time()
        join_times.append(end_time - start_time)

    print("Average time for each operation:")
    print(f"Insert: {sum(insert_times)/len(insert_times)}")
    print(f"Find: {sum(find_times)/len(find_times)}")
    print(f"Remove: {sum(remove_times)/len(remove_times)}")
    print(f"Split: {sum(split_times)/len(split_times)}")
    print(f"Join: {sum(join_times)/len(join_times)}")


if __name__ == '__main__':
    test_performance(1000)  # Change this to the desired number of operations
