'''
Get the node at the start of a cycle in a linked list

Approach:
	Start with two pointers at the root
	Advance each pointer a designated step forward until they equal each other
	Advance one pointer and count the steps until they equal each other
	Start with two pointers at the root
	Advance one of the pointers the number of steps in the cycle
	Advance both pointers until they equal eachother
'''

class node:

	def __init__(self, val, next=None):
		self.val = val
		self.next = next


def get_meeting_point(slow_node, fast_node):
	while fast_node:
		slow_node = slow_node.next
		fast_node = fast_node.next.next

		if fast_node == slow_node:
			break

	return slow_node, fast_node


def get_cycle_size(start_node, end_node):
	end_node = start_node.next
	count = 1  # check if this is the correct indexing

	while end_node != start_node:
		end_node = end_node.next
		count += 1

	return count


def get_cycle_node(root):

	'''
	returns the node at the start of a cycle

	args:
		root <node>: root node of a linked list
	returns:
		cycle_node <node>: starting node of a cycle
	'''

	if not root:
		return None
	if not root.next:
		return None

	node_1 = root
	node_2 = root.next

	node_1, node_2 = get_meeting_point(node_1, node_2)

	cycle_length = get_cycle_size(node_1, node_2)

	count = 1
	node_1 = root
	node_2 = root

	while count < cycle_length:
		node_2 = node_2.next

	while node_2 != node_1:
		node_2 = node_2.next
		node_1 = node_1.next

	return node_1




Write code to remove duplicates from an unsorted linked list 

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

'''
5 > 3 > 7 > 1 > 3 > 6 > 7

seen:5, 3, 7, 1, 6
curr:None
'''

def remove_duplicates(root):
	seen = set()

	curr = root

	while curr:
		if curr.next in seen:
			curr.next = curr.next.next
		
		seen.add(curr)
		curr = curr.next


Find nth to last item in linked list:

Approach:
	Maintain a heap of n size, return the root when you reach the end of the linked list

from collections import deque

def get_item(n, root):

	queue = deque()

	node = root

	while node:
		if len(queue) >= n:
			queue.popleft()
			
		queue.append(node)
		node = node.next




