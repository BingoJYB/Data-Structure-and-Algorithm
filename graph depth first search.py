class Node:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children
        self.visited = False


def depth_first_search(node):
    print(node.data, end=' ')
    node.visited = True
    if node.children is not None:
        for child in node.children:
            if child.visited is False:
                depth_first_search(child)


if __name__ == '__main__':
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node0.children = [node1, node4, node5]
    node1.children = [node3, node4]
    node2.children = [node1]
    node3.children = [node2, node4]

    print('depth-first search:', end=' ')
    depth_first_search(node0)
