# Treaps_Python
Treaps implementation in Python that  attempts to keep a binary tree balanced by maintaining a priority heap using randomly generated values. Includes full-coverage and stress tests.

A treap (pronounced like "tree" and "heap" combined) is a data structure that combines the properties of both binary search trees (BSTs) and binary heaps. In a treap, each node has both a key (which satisfies the BST property) and a priority (which satisfies the heap property). The priority is usually assigned randomly, creating a balanced binary tree structure. Treaps are used in various applications, including randomized algorithms and data structures where both searching and priority-based operations are important.

Here's a basic overview of how treaps work in Python:

Node Structure: Each node in the treap contains two pieces of information:

A key: This value is used to maintain the BST property. The keys follow the ordering such that nodes to the left have smaller keys, and nodes to the right have larger keys.



A priority: This is a randomly assigned value used to maintain the heap property. The priorities are typically generated uniformly at random when inserting nodes.
Rotation: To maintain the properties of the treap, you might need to perform rotations (similar to AVL or Red-Black trees). Rotations can be either left-rotations or right-rotations. These rotations are used to adjust the tree when nodes are inserted or deleted to ensure that the tree remains balanced.

Operations:

Insertion: When you insert a node with a given key and priority, it is placed in the tree according to the BST property. Then, rotations are performed if needed to maintain the heap property.



Deletion: You can delete a node by its key. This involves finding the node and removing it, then reorganizing the tree to maintain both properties.
Searching: You can search for a node in a treap just like in a standard BST, by comparing the key you're looking for with the keys in the tree.

Treaps can be implemented in Python using object-oriented programming. And in this Repo there is a simplified example of how to create a basic treap structure
