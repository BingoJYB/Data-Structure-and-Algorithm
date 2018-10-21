class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

class Stack:
    __top = None
    
    def push(self, data):
        node = Node(data)
        node.next = self.__top
        self.__top = node
        
    def pop(self):
        if self.__top == None:
            raise Exception('No data in stack!')
        
        data = self.__top.data
        self.__top = self.__top.next
        
        return data
    
    def peek(self):
        if self.__top == None:
            raise Exception('No data in stack!')
        
        return self.__top.data
    
    def isEmpty(self):
        return self.__top == None

