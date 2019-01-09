Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].



1) Ask Questions
	this is valid? [[1, 2, [3, 4, [5, 6], 7], 8], 9]
	arr[0] == list
	arr[0][0] == int
	arr[0][2] == list
	arr[0][2][0] == int
	arr[0][2][2] == list
	arr[0][2][2][0] == int

2) Rough approach

	create a stack to hold lists
	add current list to stack

	while there is values in the stack
		pop off the most recentely added
		for element in list:
			if the element is a list, add the current list back to the stack
			move on with this list



class flatten:
	'''
	Flattens a nested list: [1,[4,[6]]]


	>>> flatten([1,[4,[6]]])
	[1, 4, 6]

	'''

	Stack: [[1,[4,[6]]]]
	curr : [[1],[4,[6]]]
	N 	 : 2
	i 	 : 0
	elem : 1


	def __init__(self, arr):

		self.stack = []
		self.stack.append([arr, 0]) 


	def next(self):
		if self.hasNext():
			nested_list, curr_idx = self.stack[-1]
			self.stack[-1][1] += 1
			return nested_list[curr_idx]

	def hasNext(self):

		while self.stack:
			nested_list, curr_idx = self.stack[-1]

			if curr_idx == len(nested_list):  # No More Values in this List
				self.stack.pop()

			else:
				element = nested_list[curr_idx]

				if isinstance(element, int):
					return True

				self.stack[-1][1] += 1  # increase the index location on this nested list
				self.stack.append([element, 0])  # add this nested element

		return False
		

if __name__ == '__main__':
	import doctest
	doctest.TestMod()




when calling Next(), check for hasNext:
	access the stack (containing lists, and index locations)
	while there are values in the stack:
		peak and retrieve the most recent list and index retrieval location from the stack
		if this index equals the length of the most recent list (as in we've reached the end of this nested list):
			remove the list
		otherwise,
			create a variable to retrieve the index value form the nested list
			if this is an integer, return True
			otherwise, increase the index and add this list to the stack with the index starting at zero

	at the end, return False

get the most recent list and index location from the stack
increase the index location on the stack
return the indexed item from the most recent nested list


class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
            
    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
