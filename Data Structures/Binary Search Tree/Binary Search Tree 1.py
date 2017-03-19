class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent

    def hasleft(self):
        return self.left

    def hasright(self):
        return self.right

    def isleft(self):
        return self.parent and self.parent.left == self

    def isright(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def replace(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left = lc
        self.right = rc

        # Reassings the children
        # to the new parent
        if self.hasleft():
            self.left.parent = self
        if self.hasright():
            self.right.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if not self.root:
            self.root = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size = self.size + 1

    def _put(self, key, val, current):

        if key < current.key:

            if current.hasleft():
                self._put(key, val, current.left)
            else:
                current.left = TreeNode(key, val, parent=current)
        else:
            if current.hasright():
                self._put(key, val, current.right)
            else:
                current.right = TreeNode(key, val, parent=current)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, current):
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        else:
            return self._get(key, current.right)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isleft():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasleft():
                if self.isleft():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isleft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def findSuccessor(self):
        """

        """
        succ = None
        if self.hasright():
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.isleft():
                    succ = self.parent
                else:
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
        if current.isLeaf():  # leaf
            if current == current.parent.left:
                current.parent.left = None
            else:
                current.parent.right = None
        elif current.hasBothChildren():  # interior
            # succ = current.findSuccessor()
            succ = current.right.findMin()
            succ.spliceOut()
            current.key = succ.key
            current.value = succ.value

        else:  # this node has one child
            if current.hasleft():
                if current.isleft():
                    current.left.parent = current.parent
                    current.parent.left = current.left
                elif current.isright():
                    current.left.parent = current.parent
                    current.parent.right = current.left
                else:
                    current.replace(current.left.key,
                                    current.left.value,
                                    current.left.left,
                                    current.left.right)
            else:
                if current.isleft():
                    current.right.parent = current.parent
                    current.parent.left = current.right
                elif current.isright():
                    current.right.parent = current.parent
                    current.parent.right = current.right
                else:
                    current.replace(current.right.key,
                                    current.right.value,
                                    current.right.left,
                                    current.right.right)


mytree = BinarySearchTree()
mytree.put(6, 'apple')
mytree.put(2, 'banana')
print(mytree.get(2))
