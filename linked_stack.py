# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:49:57 2019

@author: qwer_mt

基于链表的栈
"""
from typing import Optional

class Node():
    def __init__(self, data:int, next=None):
        self._data = data
        self._next = next
        
class LinekedStack():
    def __init__(self):
        self._top : Node = None
    def push(self, value:int):
        '''链表头插入'''
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top
    def pop(self) -> Optional[int]:
        '''链表头删除'''
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value
    def __repr__(self) -> str:
        '''链表转字符串'''
        current = self._top
        nums =[]
        while current:
            nums.append(current._data)
            current = current._next
        return "".join(f"{num}]"for num in nums)
    
if __name__ == "__main__":
    stack = LinekedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
        
        

