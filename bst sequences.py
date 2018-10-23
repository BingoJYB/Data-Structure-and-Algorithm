'''
    BST Sequences: A binary search tree was created by traversing through an array from
    left to right and inserting each element. Given a binary search tree with distinct
    elements, print all possible arrays that could have led to this tree.
'''


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_children(self):
        children = []

        if self.left is not None:
            children.append(self.left)

        if self.right is not None:
            children.append(self.right)

        return children


def bst_sequences(nodes):
    result = []

    for node in nodes:
        choices = [n for n in nodes if n != node]
        choices = choices + node.get_children()

        if len(choices) > 0:
            for s in bst_sequences(choices):
                result.append([node.data] + s)
        else:
            result.append([node.data])

    return result


if __name__ == '__main__':
    node0 = Node(4)
    node1 = Node(2)
    node2 = Node(5)
    node3 = Node(1)
    node4 = Node(3)
    node5 = Node(6)

    node0.left = node1
    node0.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5

    print(bst_sequences([node0]))
