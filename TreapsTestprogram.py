

# This program prompts the user for the desired operation and corresponding
#     inputs, performs the operation on the treap, and prints the resulting
# treap configuration using an in -order traversal. The program continues to
# prompt the user for operations until the user enters "quit".


# !pip install treap #UNCOMMENT TO INSTALL TREAP IN YOUR MACHINE
from treap import Treap


def print_treap(node):
    if node is None:
        return
    print_treap(node.left)
    print(node.key, node.priority)
    print_treap(node.right)


t = Treap()

while True:
    print("Enter operation (insertWithPriority, insert, remove, find, split, join, or quit):")
    operation = input().strip()

    if operation == "insertWithPriority":
        key = input("Enter key: ")
        priority = float(input("Enter priority: "))
        t.insert_with_priority(key, priority)
        print_treap(t.root)

    elif operation == "insert":
        key = input("Enter key: ")
        t.insert(key)
        print_treap(t.root)

    elif operation == "remove":
        key = input("Enter key: ")
        try:
            priority = t.remove(key)
            print("Removed key", key, "with priority", priority)
            print_treap(t.root)
        except KeyError:
            print("Key", key, "not found")

    elif operation == "find":
        key = input("Enter key: ")
        priority = t.find(key)
        if priority == 0:
            print("Key", key, "not found")
        else:
            print("Priority of key", key, "is", priority)

    elif operation == "split":
        key = input("Enter key: ")
        t2 = t.split(key)
        print("Treap containing keys larger than", key)
        print_treap(t2.root)
        print("Treap containing keys smaller than or equal to", key)
        print_treap(t.root)

    elif operation == "join":
        print("Enter keys to join separated by spaces:")
        keys = input().split()
        t2 = Treap()
        for key in keys:
            t2.insert(key)
        t.join(t2)
        print_treap(t.root)

    elif operation == "quit":
        break

    else:
        print("Invalid operation")
