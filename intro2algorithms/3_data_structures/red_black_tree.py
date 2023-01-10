RED, BLACK = 0, 1

"""
    A red-black tree is a BST that has the following properties:
    
    1. Every tree node is either black or red
    2. The root is black
    3. Every leaf node is black
    4. If a node is red, then its two child nodes are black
    5. For every node, there are the same number of black nodes from that node to all its child leaf nodes.
    
    Theorem: A red-black tree with n nodes has a maximum height of 2*lg(n+1).
    
    Therefore, for look-ups, red-black tree is at worst 2 times slower than AVL tree, but it has faster insertion
    and removal. AVL trees are more often used in databases whereas r-b trees are used for general purposes.
"""


class TreeNode():
    def __init__(self, color=None, key=None):
        self.color = color
        self.key = key
        self.left = None
        self.right = None
        self.p = None


class RBTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(color=BLACK, key=key)  # property 2: root color is BLACK
            return

    """ helper functions """

    def left_rotate(self, x):
        """ do a left rotation at node x """
        y = x.right                 # set y
        x.right = y.left            # turn y's subtree into x's right subtree
        if y.left is not None:
            y.left.p = x
        y.p = x.p                   # link x's parent to y
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x                  # put x on y's left
        x.p = y

    def right_rotate(self, x):
        """ do a right rotation at node x """
        y = x.left                  # set y
        x.left = y.right            # turn y's subtree into x's left subtree
        if y.right is not None:
            y.right.p = x
        y.p = x.p                   # link x's parent to y
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x                  # put x on y's right
        x.p = y


