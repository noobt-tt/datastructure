'''
判断是否是回文字符串
'''
from SinglyLinkedList import Node
from SinglyLinkedList import SinglyLinkedList

def reverse(slow):
pre = None
	while solw:
		tmp = slow.next
		slow.next = pre
		pre = slow
		slow = tmp
	return pre

def is_palindrome(l):
	l.print_all()
	fast = l.__head
	slow = l.__head
	while fast.next:
		fast = fast.next.next
		slow = slow.next

	end_node = reverse(slow)
	start_node = l.__head
	is_palin = True
	while start_node and end_node:
		if start_node.data == end_node.data:
			start_node = start_node.next
			end_node = end_node.next
		else:
			is_palin = False
			break
	return is_palin

if __name__=='__main__':
	test_str_arr = ['ab', 'aa', 'aba', 'abba', 'abcba']
	for str in test_str_arr:
		l = SinglyLinkedList()
		for i in str:
			l.insert_to_head(i)
		print(is_palindrome(l))