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

    def find_by_index(self, index):
        node = self.__head
        pos = 0
        while node!=None and pos!=index:
            node = node.next
            pos += 1
        return node

    def insert_to_head(self, value):
    	'''链表头部插入'''
    	node = Node(value)
    	node.next = self.__head
    	self.__head = node

    def insert_after(self, node, value):
    	'''指定节点后插入'''
    	if node==None:
    		return
    	new_node = Node(value)
    	new_node.next = node.next
    	node.next = new_node

    def insert_before(self, node, value):
    	'''指定节点前插入'''
    	if self.__head==None or node==None:
    		return
    	if node==self.__head:
    		self.insert_to_head(value)
    		return
    	new_node = Node(value)
    	pro = self.__head
    	not_find = False
    	while pro.next != node:
    		if pro.next == None:
    			not_find = True
    			break
    		else:
    			pro = pro.next
    	if not_find == False:
    		new_node.next = pro.next
    		pro.next = new_node

    def delete_by_node(self, node):
    	'''删除指定节点'''
    	if self.__head == None:
    		return
    	if node == self.__head:
    		self.__head = node.next
    		return
    	pro = self.__head
    	not_find = False
    	while pro.next != node:
    		if pro.next == None:
    			not_find = True
    			break
    		else:
    			pro = pro.next
    	if not_find == False:
    		pro.next = node.next

    def delete_by_value(self, value):
    	'''删除存储指定数据的节点'''
    	if self.__head == None:
    		return
    	if self.__head.data == value:
    		self.__head = self.__head.next
    	pro = self.__head
    	node = self.__head.next
    	not_find = False
    	while node.data != value:
    		if node==None:
    			not_find = True
    			break
    		else:
    			pro = pro.next
    			node = node.next
    	if not_find == False:
    		pro.next = node.next

    def delete_last_N_node(self, n):
    	'''删除倒数第N个节点'''
    	fast = self.__head
    	slow = self.__head
    	step = 0
    	while step <= n:
    		fast = fast.next
    		step += 1
    	while fast.next!=None:
    		fast = fast.next
    		slow = slow.next
    	slow.next = slow.next.next

    def delete_mid_node(self):
    	'''删除中间节点'''
    	fast = self.__head
    	slow = self.__head
    	while fast.next!=None:
    		fast = fast.next.next
    		slow = slow.next
    	return slow

    def create(self, value):
    	return Node(value)

    def print_all(self):
    	'''打印链表'''
    	if self.__head == None:
    		pritn('当前链表是空哒！')
    		return
    	pos = self.__head
    	while pos!=None:
    		print(str(pos.data)+'--->',end='')
    		pos = pos.next

    def _reversed_with_two_node(self, pre, node):
    	'''翻转相邻两个节点'''
    	tmp = node.next
    	node.next = pre
    	pre = node
    	node = tmp
    	return(pre, node)

    def reversed_self(self):
    	'''翻转链表自身'''
    	if self.__head == None or self.__head.next == None:
    		return
    	pre = self.__head
    	node = self.__head.next
    	while node!=None:
    		pre, node = self._reversed_with_two_node(pre, node)
    	self.__head.next = None
    	self.__head = pre

    def has_ring(self):
    	'''检查链表是否有环'''
    	fast = self.__head
    	slow = self.__head
    	while fast.next!=None:
    		fast = fast.next.next
    		slow = slow.next
    		if fast == slow:
    			return True
    	return False

    







































