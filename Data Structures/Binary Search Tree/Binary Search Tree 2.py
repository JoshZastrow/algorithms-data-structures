class node():

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def isRoot(self):
        return not self.parent

    def hasChildren(self):
        return (self.left or self.right)

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right

    def hasBoth(self):
        return self.left and self.right

    def hasOneChild(self):
        return (self.left and not self.right) or (self.right and not self.left)

    def replace(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent

        if self.hasLeft():
            self.left.parent = self
        if self.hasRight():
            self.right.parent = self

    def isRight(self):
        return self.parent.right == self

    def isLeft(self):
        return self.parent.left == self


class BST:

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

        if not self.root:
            self.root = node(key, value)
        else:
            self._put(key, value, self.root)

        self.size = self.size + 1

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

            current.replace(key, value, current.left, current.right, current)

        else:
            return KeyError('Key is not the correct data type.')

    def get(self, key):

        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
            else:
                return None
        else:
            return None

    def _get(self, key, current):

        if key == current.key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        elif key > current.key:
            return self._get(key, current.right)
        else:
            return KeyError('Key is not of correct data type')

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):

        if self._get(key):
            return True
        else:
            return False

    def delete(self, key):

        if self.size > 1:
            NodeToRemove = self._get(key, self.root)
            if NodeToRemove:
                self.remove(NodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Key not found')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Key not found')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self):
        # Condition if node is a leaf
        if self.hasChildren():
            if self.hasLeft():
                if self.isLeft():
                    self.parent.left = self.left
                elif self.isRight():
                    self.parent.right = self.left
                self.left.parent = self.parent

            elif self.hasRight():
                if self.isLeft():
                    self.parent.left = self.right
                elif self.isRight():
                    self.parent.right = self.right
                self.right.parent = self.parent
        else:
            if self.isLeft():
                self.parent.left = None
            elif self.isRight():
                self.parent.right = None

    def findSuccessor(self):
        succ = None
        if self.hasRight():
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.isLeft():
                    succ = self.parent
                elif self.isRight():
                    self.parent.right = None
                    succ = self.parent.findSuccessor()
                    self.parent.right = self
        return succ

    def findMin(self):
        current = self
        while current.hasleft():
            current = current.left
        return current

    def remove(self, current):
        if current.isLeaf():
            if current.isLeft():
                current.parent.left = None
            elif current.isRight():
                current.parent.right = None
        elif current.hasBoth():
            succ = current.findSuccessor()
            succ.spliceOut()
            current.key = succ.key
            current.value = succ.value


mytree = BST()
mytree.put(6, 'apple')
mytree.put(2, 'banana')
print(mytree.get(2))
