class Node:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.lchild)
        print(node.data)
        in_order_traversal(node.rchild)


def pre_order_traversal(node):
    if node is not None:
        print(node.data)
        pre_order_traversal(node.lchild)
        pre_order_traversal(node.rchild)


def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.lchild)
        post_order_traversal(node.rchild)
        print(node.data)


if __name__ == '__main__':
    node5 = Node(15)
    node4 = Node(7)
    node3 = Node(3)
    node2 = Node(20, node5)
    node1 = Node(5, node3, node4)
    root = Node(10, node1, node2)

    print('pre-order traversal:')
    pre_order_traversal(root)

    print('')

    print('in-order traversal:')
    in_order_traversal(root)

    print('')

    print('post-order traversal:')
    post_order_traversal(root)
