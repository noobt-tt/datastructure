class Node():
    def __init__(self,data,next=None):
        self.__data = data
        self.__next = next
    def data(self):
        return self._data
    def data(self,data):
        self.__data = data
    def next(self):
        return self._next
    def next(self,next):
        self.__next = next
class SinglyLinkedList():
    def __init__(self):
        self.__head = None
    def find_by_value(self, value):
        '''按照数据值查找'''
        node = self.__head
        while node!=None and node.data!=value:
            node = node.next
        return node
    def find_by_index(self,index):
        node = self.__head
        pos = 0
        while node!=None and node.data!=value:
            node = node.next
            pos += 1
        return node