class node():

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def isLeaf(self):
        return not (self.left and self.right)

    def isRoot(self):
        return not self.parent

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right

    def isRight(self):
        return self.parent.right == self

    def isLeft(self):
        return self.parent.left == self

    def hasBothChildren(self):
        return self.left and self.right

    def hasOneChild(self):
        return (self.left and not self.right) or (not self.left and self.right)

    def replaceNode(self, key, val, lc, rc):
        self.key = key
        self.value = val
        self.left = lc
        self.right = rc

        if self.hasLeft():
            self.left.parent = self
        if self.hasRight():
            self.right.parent = self
    def findSuccessor(self):
        succ = None
        if self.hasRight():
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.isleft():
                    succ = self.parent


    def findMin(self):
        current = self
        while current.hasLeft():
            current = current.left
        return current

    def splice():
        pass



class Tree():

    def __init__(self):
        self.root = None
        self.size = 0

    def __iter__(self):
        return self.root.__iter__(self)

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = node(key, value)

        self.size += 1

    def _put(self, key, value, current):
        if key < current.key:
            if current.hasLeft():
                self._put(key, value, current.left)
            else:
                current.left = node(key, value, parent=current)
        elif key > current.key:
            if current.hasRight():
                self._put(key, value, current.right)
            else:
                current.right = node(key, value, parent=current)
        elif key == current.key:
            current.replaceNode(key, value, current.left, current.right)
        else:
            return KeyError("key is not correct data type")

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            foundNode = self._get(key, self.root)
            if foundNode:
                return foundNode.value
            else:
                return None
        else:
            return None

    def _get(self, key, current):
        if current:
            if key == current.key:
                return current
            elif key < current.key:
                return self._get(key, current.left)
            elif key > current.key:
                return self._get(key, current.right)
        else:
            return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:  # Conditions if it's more than 1 root node
            node = self._get(key, self.root)  # Search for Node 2 Del
            if node:  # Condition if found
                self.remove(node)  # Call a removal function
                self.size -= 1  # Decrease the size
            else:
                return KeyError('key not found')  # Return error
        elif self.size == 1 and self.root.key == key:  # One Node
            self.root = None  # Get rid of it
        else:
            return KeyError('Error: key not found in tree')

    def remove(self, node):  # Removal Function
        if node.isLeaf():  # Condition on if it's a leaf
            if node.isLeft():  # Condition if it's left child
                node.parent.left = None  # Get rid of link to parent
            elif node.isRight():
                node.parent.right = None
            node = None  # Make the node disappear
        elif node.hasOneChild():  # Condition for one child
            if node.hasLeft():  # Has left child
                if node.isLeft():  # Is left child, connect to parent
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.isRight():  # Is right child, connect to p.
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:  #  No parent, means it's the root, replace
                    self.root.replaceNode(node.left.key,
                                          node.left.value,
                                          node.left.left,
                                          node.left.right)
            elif node.hasRight():  # Same, but for a right child
                if node.isLeft():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.isRight():
                    node.right.parent = node.parent
                    node.parent.right = node.right
        elif node.hasBothChildren():
            succ = node.findSuccessor()  # Find the node to replace
            succ.splice()  # Remove the node
            node.key = succ.key
            node.value = succ.value  # Assign the successor values
