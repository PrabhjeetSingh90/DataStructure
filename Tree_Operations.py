#-------------------------------------------------------------------------------
#
# Author:      prabhjeet Singh
#
# Purpose : The Puspose of this code is to demonstrate basic operations on
#           various types of tree structures.
#
#-------------------------------------------------------------------------------
import Queue

class Dnode:
    __value = None
    __leftchild = None
    __rightchild = None
    def __init__(self, value = None, leftchild = None, rightchild = None):
        self.__value = value
        self.__leftchild = leftchild
        self.__rightchild = rightchild

    # Get Functions
    def getvalue(self):
        return self.__value
    def getleftchild(self):
        return self.__leftchild
    def getrightchild(self):
        return self.__rightchild

    # Set Functions
    def setvalue(self, value= None):
        self.__value = value
    def setleftchild(self, leftchild = None):
        self.__leftchild = leftchild
    def setrightchild(self, rightchild = None):
        self.__rightchild = rightchild

class AVLDnode(Dnode):
    __heigth = None
    def __init__(self, value = None, height = None, leftchild = None, rightchild = None):
        self.__heigth = height
        Dnode.__init__(self, value, leftchild, rightchild)

    # Get Functions
    def getheigth(self):
        return self.__heigth

    # Set Functions
    def setheight(self, height = None):
        self.__heigth = height

class display:
    def __int__(self):
        pass

    def display(self, node= None, type = "inorder"):
        #Displaying in Inorder Traversal
        if type == "inorder":
            if node:
                self.display(node.getleftchild(), "inorder")
                print (" inorder node value = " + str(node.getvalue()))
                self.display(node.getrightchild(), "inorder")
        elif type == "preorder":
            if node:
                print (" preorder node value = " + str(node.getvalue()))
                self.display(node.getleftchild(), "preorder")
                self.display(node.getrightchild(), "preorder")
        elif type == "postorder":
            if node:
                self.display(node.getleftchild(), "postorder")
                self.display(node.getrightchild(), "postorder")
                print (" postorder node value = " + str(node.getvalue()))

# Complete Binary Tree
class binarytree:
    __head = None
    def __init__(self, node = None):
        self.__head = node

    def gethead(self):
        return self.__head

    def sethead(self, node= None):
        self.__head = node

    def insert(self, node = None, key = None):
        # Create a Queue to Store Node while traversing the tree level order
        # Queue Size will create a issue with scalability.
        Q = Queue.Queue(100)
        # if root is none. This is first node to insert
        if (node == None):
            node = Dnode(key)
            return node
        else: # Not the first Node
            Q.put(node) # Add head to Queue

            while(Q.empty() == False): # Loop until Queue is Empty
                # Fetch the first node from Queue
                newnode = Q.get()
                 # if left node is null than insert and break loop
                if newnode.getleftchild() == None:
                    newnode.setleftchild(Dnode(key))
                    break
                else: # Else push left node address to queue
                    Q.put(newnode.getleftchild())

                # if right node is null than insert and breakloop
                if newnode.getrightchild() == None:
                    newnode.setrightchild(Dnode(key))
                    break
                else: # Else insert right node address to Queue
                    Q.put(newnode.getrightchild())
        return node # Return the head value back.

#############
# This is an ordered binary tree where all the elements in the left subtree is
# less than root and all the elements on right subtree is  greater than root
# for every node.
###########
class binarysearchtree:
    __head = None
    def __init__(self, node = None):
        self.__head = node

    def gethead(self):
        return self.__head

    def sethead(self, node= None):
        self.__head = node

    def insert(self, node = None, key = None):
        if (node == None):
            node = Dnode(key)
        else:
            if(node.getvalue() > key):
                node.setleftchild(self.insert(node.getleftchild(),key))
            elif(node.getvalue() < key):
                node.setrightchild(self.insert(node.getrightchild(),key))
        return node


#############
# This is a self balancing Binary Search tree where the height difference
# between left subtree and right subtree is not more than one for any node.
###########
class avltree:
    __head = None

    def __inti__(self, node = None):
        self.__head = node

    def gethead(self):
        return self.__head

    def sethead(self, node = None):
        self.__head = node

    def insert(self, node = None, key = None):
        pass

    def __rotateleft(self, node= None):
        newhead = node.getrightchild()
        temp = newhead.getleftchild()

        newhead.setleftchild(node)
        node.setrightchild(temp)

        newheadL = newhead.getleftchild()
        newheadR = newhead.getrightchild()

        newhead.setheight(1 + max(newheadL.getheight(), newheadR.getheight()))

        nodeL = node.getleftchild()
        nodeR = node.getrightchild()

        node.setheight(1 + max(nodeL.getheight(), nodeR.getheight()))

        return newhead

    def __rotateright(self, node = None):
        newhead = node.getleftchild()
        temp = newhead.getrightchild()

        newhead.setrightchild(node)
        node.setleftchild(temp)

        newheadL = newhead.getleftchild()
        newheadR = newhead.getrightchild()

        newhead.setheight(1 + max(newheadL.getheight(), newheadR.getheight()))

        nodeL = node.getleftchild()
        nodeR = node.getrightchild()

        node.setheight(1 + max(nodeL.getheight(), nodeR.getheight()))

        return newhead

    def __getbalance(self, node = None):
        if node == None:
            return 0;
        else:
            leftnode = node.getleftchild()
            rightnode = node.getrightchild()
            bal = leftnode.getheight() - rightnode.getheight()
            return bal



class redblacktree:
    pass

class splaytree:
    pass

class narytree:
    pass

class triestruct:
    pass

class suffixtree:
    pass

class huffmantree:
    pass

class heapstruct:
    pass

class testcases:
    def __init__(self):
        self.disp = display()

    def TC_binarysearchtree(self):
        # Create Instance Of Binary Search Tree Class
        bst = binarysearchtree()
        # Generating Binary Search Tree by inserting element by element
        bst.sethead(bst.insert(bst.gethead(),10))
        bst.sethead(bst.insert(bst.gethead(),20))
        bst.sethead(bst.insert(bst.gethead(),5))
        bst.sethead(bst.insert(bst.gethead(),40))
        bst.sethead(bst.insert(bst.gethead(),50))
        bst.sethead(bst.insert(bst.gethead(),100))
        bst.sethead(bst.insert(bst.gethead(),1))
        bst.sethead(bst.insert(bst.gethead(),6))
        # Display Binary Search Tree
        self.disp.display(bst.gethead(), "inorder")
        self.disp.display(bst.gethead(), "preorder")
        self.disp.display(bst.gethead(), "postorder")

    def TC_binarytree(self):
        #create instance of binary tree
        btree = binarytree()
        # Generate Binary Tree by inserting element by element
        btree.sethead(btree.insert(btree.gethead(), 50))
        btree.sethead(btree.insert(btree.gethead(), 30))
        btree.sethead(btree.insert(btree.gethead(), 40))
        btree.sethead(btree.insert(btree.gethead(), 10))
        # Display Binary Tree
        self.disp.display(btree.gethead(), "inorder")



def main():
    tc = testcases()
    tc.TC_binarysearchtree()
    tc.TC_binarytree()

if __name__ == '__main__':
    main()
