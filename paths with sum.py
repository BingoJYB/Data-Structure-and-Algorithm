'''
    Return all downward paths through a tree whose nodes sum to a target value.
'''


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_path_num(node, target, currsum):
    if node is None:
        return 0

    currsum = currsum + node.data
    path_num = 0

    if currsum == target:
        path_num = path_num + 1

    path_num = path_num + get_path_num(node.left, target, currsum)
    path_num = path_num + get_path_num(node.right, target, currsum)

    return path_num


def paths_with_sum(node, target):
    if node is None:
        return 0

    path_num = get_path_num(node, target, 0)
    left_path_num = paths_with_sum(node.left, target)
    right_path_num = paths_with_sum(node.right, target)

    return path_num + left_path_num + right_path_num


if __name__ == '__main__':
    node0 = Node(10)
    node1 = Node(5)
    node2 = Node(-3)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(11)
    node6 = Node(3)
    node7 = Node(-2)
    node8 = Node(1)

    node0.left = node1
    node0.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.right = node8

    print(paths_with_sum(node0, 8))
