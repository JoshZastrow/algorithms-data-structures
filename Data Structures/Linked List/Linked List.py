import sys


class node():

    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode


    def update(self, newData):
        self.data = newData

    def __str__(self):
        return str(self.data)


class linked_List():

    def __init__(self, head=None):
        if head:
            self.head = node(head)
        else:
            self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = self.head
        self.head = node(item)
        self.head.next = temp

    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


    def search(self, item):

        current = self.head
        index = 0
        while current:
            if current.data == item:
                return True
            else:
                index += 1
                current = current.next
        return False

    def remove(self, item):

        if self.head:

            current = self.head

            # handle head case
            if current.data == item:
                self.head = self.head.next

            while current.next is not None:
                if current.next.data == item:

                    current.next = current.next.next

                else:
                    current = current.next



    def deleteDups(self):

        the_list_already = set()

        curr_node = self.head

        while curr_node.next:

            if curr_node.next.data in the_list_already:
                print('removing', curr_node.next.data)
                curr_node.next = curr_node.next.next

            else:

                the_list_already.add(curr_node.data)
                curr_node = curr_node.next
        return

    def deleteDups_inplace(self):

        if self.head:

            curr_node = self.head

            while curr_node.next:

                runner = self.head

                while runner != current.next:

                    if runner.data == curr_node.next.data:
                        curr_node.next = curr_node.next.next
                    else:
                        runner = runner.next

                curr_node = curr_node.next



def n_to_last(n, headNode):

    if not headNode.head or n < 1:
        return None

    p1 = headNode.head
    p2 = headNode.head

    # get p2 to be n elements away from p1 (p1 is the nth element before p2)
    for j in range(n):
        if not p2:
            return None
        p2 = p2.next

    # move up both points until p2 is last element:

    while p2:
        p1 = p1.next
        p2 = p2.next



x = linked_List()
print(x)
x.add(1)
x.add(23)
x.add(2)
x.add(5)
x.add(1)
x.add(4)
x.add(5)
x.deleteDups_inplace()
