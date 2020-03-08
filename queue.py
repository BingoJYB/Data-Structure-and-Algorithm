class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

class Queue:
    __first = None
    __last = None
    
    def add(self, data):
        node = Node(data)
        
        if self.__first == None:
            self.__first = node
            self.__last = self.__first
        else:
            self.__last.next = node
            self.__last = node
        
    def remove(self):
        if self.__first == None:
            raise Exception('No data in stack!')
        
        data = self.__first.data
        self.__first = self.__first.next
        
        if self.__first == None:
            self.__last = None
        
        return data
    
    def peek(self):
        if self.__first == None:
            raise Exception('No data in stack!')
        
        return self.__first.data
    
    def isEmpty(self):
        return self.__first == None

