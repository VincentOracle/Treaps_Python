
# CS 610 Spring 2023
# Instructor: Ravi Varadarajan
# Performance of Treaps Project
#Date: 2/MAY/2023

# !pip install treap #UNCOMMENT TO INSTALL TREAP IN YOUR MACHINE

# Import the random library
import random


class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None


class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

# define the Treap class which will contain the main operations


class Treap:
    def __init__(self):
        self.root = None
        self.size = 0

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child

    def insertWithPriority(self, key, priority):
        def _insert(node):
            if not node:
                return Node(key, priority)
            if key < node.key:
                node.left = _insert(node.left)
                if node.left.priority > node.priority:
                    node = self._rotate_right(node)
            elif key > node.key:
                node.right = _insert(node.right)
                if node.right.priority > node.priority:
                    node = self._rotate_left(node)
            else:
                node.priority = priority
            return node

        self.root = _insert(self.root)
        self.size += 1

    def insert(self, key):
        self.insertWithPriority(key, random.random())

    def remove(self, key):
        def _remove(node):
            if not node:
                raise KeyError(str(key))
            if key < node.key:
                node.left = _remove(node.left)
            elif key > node.key:
                node.right = _remove(node.right)
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            elif node.left.priority > node.right.priority:
                node = self._rotate_right(node)
                node.right = _remove(node.right)
            else:
                node = self._rotate_left(node)
                node.left = _remove(node.left)
            return node

        self.root = _remove(self.root)
        self.size -= 1

    def find(self, key):
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.priority
        return 0

    def split(self, key):
        def _split(node):
            if not node:
                return (None, None)
            if key < node.key:
                left, node.left = _split(node.left)
                return left, self._rotate_right(node) if left and left.priority > node.priority else node
            else:
                node.right, right = _split(node.right)
                return self._rotate_left(node) if right and right.priority > node.priority else node, right

        left, right = _split(self.root)
        self.root = left
        return Treap._to_treap(right)


# In the else case, since node1 has a priority less than or equal to node2,
# we want to make node2 the root of the subtree that contains node1. So we
# recursively call _join on node1 and node2.left to get the root of the left
# subtree of node2. We then set this returned node as the new left child of
# # node2. Finally, we return node2, which is now the root of the subtree containing
# both node1 and node2.

    def join(self, treap):
        def _join(node1, node2):
            if not node1 or not node2:
                return node1 or node2
            if node1.priority > node2.priority:
                node1.right = _join(node1.right, node2)
                return node1
            else:
                node2.left = _join(node1, node2.left)
                return node2
