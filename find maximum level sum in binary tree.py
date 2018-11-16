'''
    Find maximum level sum in Binary Tree
    Given a Binary Tree having positive and negative nodes, the task is to find maximum sum level in it.
'''


import math


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_level_sum(root):
    if root is None:
        return 0

    queue = [root]
    maximum = -math.inf

    while len(queue) > 0:
        count = len(queue)
        sum = 0

        while count > 0:
            node = queue.pop(0)
            count -= 1
            sum += node.data

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        maximum = max(maximum, sum)

    return maximum


root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(8)
node6 = Node(6)
node7 = Node(7)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
node5.left = node6
node5.right = node7

print(get_level_sum(root))
