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


class TreeNode:
    def __init__(self, color=None, key=None):
        self.color = color
        self.key = key
        self.left = None
        self.right = None
        self.p = None


NIL = TreeNode(color=BLACK)  # sentinel at the top and bottom of the tree


def tree_minimum(x):
    """ find minimum node (leftmost) rooted at x. """
    while x.left != NIL:
        x = x.left
    return x


class RBTree:
    def __init__(self):
        self.root = NIL

    def search(self, key):
        """ return the TreeNode object with key=key in the red-black tree. """
        x = self.root
        while x != NIL:
            if x.key == key:
                return x
            elif x.key < key:
                x = x.right
            else:
                x = x.left
        return None

    def insert(self, key):
        """ insert a new node with key=key to the red-black tree. """
        z = TreeNode(color=RED, key=key)  # z is the node to be inserted, color must be RED
        y = NIL  # y is the parent of z
        x = self.root
        while x != NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = NIL
        z.right = NIL

        # above is normal BST insertion, need to recolor the tree to maintain RB properties
        while z.p.color == RED:
            # z.p.p must exist because z.p is RED meaning that z.p is
            # not the root
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == RED:  # case 1
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:  # case 2
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = BLACK  # case 3
                    z.p.p.color = RED
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == RED:  # case 1
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:  # case 2
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = BLACK  # case 3
                    z.p.p.color = RED
                    self.left_rotate(z.p.p)

        self.root.color = BLACK

    def delete(self, key):
        z = self.search(key)  # this takes O(log(n)) time
        y = z
        y_original_color = y.color
        if z.left == NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == BLACK:
            self.delete_fixup(x)

    """ helper functions """

    def left_rotate(self, x):
        """ do a left rotation at node x """
        y = x.right  # set y
        x.right = y.left  # turn y's subtree into x's right subtree
        if y.left != NIL:
            y.left.p = x
        y.p = x.p  # link x's parent to y
        if x.p == NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x  # put x on y's left
        x.p = y

    def right_rotate(self, x):
        """ do a right rotation at node x """
        y = x.left  # set y
        x.left = y.right  # turn y's subtree into x's left subtree
        if y.right != NIL:
            y.right.p = x
        y.p = x.p  # link x's parent to y
        if x.p == NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x  # put x on y's right
        x.p = y

    def transplant(self, u, v):
        """ replace node u with node v """
        if u.p == NIL:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def delete_fixup(self, x):
        pass


def print_tree(root):
    """ visualize a red-black tree """
    if root == NIL:
        return
    print("current node:", root.key, "\tcolor:", "BLACK" if root.color == 1 else "RED  "
          , "\tp:", root.p.key, "\tleft:", root.left.key, "\tright:", root.right.key)
    print_tree(root.left)
    print_tree(root.right)


def main():
    tree = RBTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(4)
    tree.insert(5)
    tree.insert(7)
    tree.insert(8)
    tree.insert(11)
    tree.insert(14)
    tree.insert(15)
    print_tree(tree.root)


if __name__ == '__main__':
    main()
