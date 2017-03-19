class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeft(self):
        return self.left

    def hasRight(self):
        return self.right

    def isRight(self):
        return self.parent and self.parent.right == self

    def isLeft(self):
        return self.parent and self.parent.left == self

    def hasBoth(self):
        return self.left and self.right

    def hasOneChild(self):
        return (self.left and not self.right) or (self.right and not self.left)

    def isLeaf(self):
        return (not self.left and not self.right)

    def isRoot(self):
        return self.parent

    def replace(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left = lc
        self.right = rc

        # Reassign the children of this node
        # to the proper parent
        if self.hasLeft():
            self.left.parent = self
        if self.hasRight():
            self.right.parent = self

    def splice(self):
        if self.isLeaf():
            if self.isLeft():
                self.parent.left = None
            elif self.isRight():
                self.parent.right = None
        elif self.hasRight() or self.hasLeft():
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

    def findSuccessor(self):
        succ = None
        if self.hasRight():
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.isLeft():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.findSuccessor()
                    self.parent.right = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeft():
            current = current.left
        return current


class BST:

    def __init__(self):  # Initialize root and size
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
        self.size = self.size + 1  # increase the bst length

    def _put(self, key, val, current):

        if key < current.key:

            if current.hasLeft():
                self._put(key, val, current.left)
            else:
                current.left = TreeNode(key, val, parent=current)

        elif key > current.key:
            if current.hasRight():
                self._put(key, val, current.right)
            else:
                current.right = TreeNode(key, val, parent=current)

        elif key == current.key:
            current.replace(key, val, current.left, current.right)

        else:
            raise KeyError('Key is not correct data type')

    def __setitem__(self, k, v):
        self.put(k, v)

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
        if not current:  # Base Case
            return None
        else:
            if key == current.key:
                return current
            elif key < current.key:
                if current.hasLeft():
                    self._get(key, current.left)  # search left child
            elif key > current.key:
                if current.hasRight():
                    self._get(key, current.right)  # search right child
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
        if self.size > 1:
            NodeToRemove = self._get(key, self.root)
            if NodeToRemove:
                self.remove(NodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('key not found in Tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current):
        if current.isLeaf():
            if current.isLeft():
                current.parent.left = None
            elif current.isRight():
                current.parent.right = None
            current = None
        elif current.hasOneChild():
            if current.hasLeft():
                if current.isLeft():
                    current.parent.left = current.left
                    current.left.parent = current.parent
                elif current.isRight():
                    current.parent.right = current.left
                    current.left.parent = current.parent
                else:  # this is a root node, replace root
                    current.replace(current.left.key,
                                    current.left.value,
                                    current.left.left,
                                    current.left.right)

            if current.hasRight():
                if current.isLeft():
                    current.parent.left = current.right
                    current.right.parent = current.parent
                elif current.isRight():
                    current.parent.right = current.right
                    current.right.parent = current.parent
                else:  # root node with no left tree
                    current.replace(current.right.key,
                                    current.right.value,
                                    current.right.left,
                                    current.right.right)

        elif current.hasBoth():
            succ = current.findSuccessor()  # find the replacing node
            succ.splice
            current.key = succ.key
            current.value = succ.value
