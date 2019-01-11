'''
基于链表的队列
'''
from typing import Optional

class Node():
	def __init__(self, data:str, next=None):
		self.data = data
		self._next = next

class linked_Queue():
	"""docstring for linked_Queue"""
	def __init__(self):
		self._head: Optional[Node] = None
		self._tail: Optional[Node] = None

	def enqueue(self, value:str):
		'''入队'''
		new_Node = Node(value)
		if self._tail:
			self._tail._next = new_Node
		else:
			self._head = new_Node
		self._tail = new_Node

	def dequeue(self) -> Optional[str]:
		'''出队'''
		if self._head:
			value = self._head.data
			self._head = self._head._next
			if not self._head:
				self._tail = None
			return value

	def __repr__(self) -> str:
		values = []
		current = self._head
		while current:
			values.append(current.data)
			current = current._next
		return "->".join(value for value in values)

if __name__=="__main__":
	q = linked_Queue()
	for i in range(10):
		q.enqueue(str(i))
	print(q)

	for i in range(3):
		q.dequeue()
	print(q)

	q.enqueue("7")
	q.enqueue("8")
	print(q)