import pytest


def isBalanced(tree):
    '''
    Function to determine if the tree is balanced, such
    that no two leaf nodes differ in distance from the
    node by more than 1.

    input: a tree
    output: True/False statement on whether the tree is balanced

    '''

    if max_length(tree.head) - min_length(tree.head) > 1:
        return True
    else:
        return False

def max_length(node):
    '''
    Methodology:
    If the node does not exist, then return 0. If the node exists,
    return the longer length of it's two children + the node
    '''

    if not node:
        return 0

    else:
        return max(max_length(node.left), max_length(node.right)) + 1


def min_length(node):

    if not node:
        return 0

    else:
        return min(min_length(node.left), min_length(node.right)) + 1


def print_order(tree):
    '''
    BFS printout of a tree. Function uses recursion to get max height
    of tree, then for each level prints the nodes on that level.
    '''
    h = get_height(tree)

    for i in range(1, h):
        print_level(tree, i)


def print_level(tree, level):
    '''
    function prints the node if on the correct level (1). Otherwise,
    recurse to the children and subtract a level.
    '''
    if not tree:
        return

    elif level == 1:
        print(tree.data)

    else:
        print_level(tree.left, level-1)

        print_level(tree.right, level-1)


def get_height(node):

    if node is None:
        return 0

    if:
        # Compute height of each subtree
        lheight = get_height(node.left)
        rheight = get_height(node.right)

        return max(lheight, rheight) + 1
