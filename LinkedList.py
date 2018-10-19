'''
    LinkedList - insert, delete, update, search
'''

class Node:
    data = 0
    next = None
    
    def __init__(self, data):
        self.data = data
    

def insert(header, node, pos):
    h = header
    
    if pos == 0:
        node.next = h
        header = node
        
        return header
    
    for _ in range(pos-1):
        h = h.next
        
    temp = h.next
    h.next = node
    node.next = temp
        
    return header


def delete(header, pos):
    h = header
    
    if pos == 0:
        header = header.next
        return header
    
    for _ in range(pos-1):
        h = h.next
        
    h.next = h.next.next
        
    return header


def search(header, pos):
    h = header
    
    for _ in range(pos):
        h = h.next
    
    print(h.data)


def update(header, data, pos):
    h = header
    
    for _ in range(pos):
        h = h.next
        
    h.data = data
    
    return header

