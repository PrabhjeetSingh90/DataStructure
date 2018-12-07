#-------------------------------------------------------------------------------
#
# Author:      prabhjeet Singh
#
# Purpose : The Puspose of this code is to demonstrate basic operations on
#           various types of tree structures.
#
#-------------------------------------------------------------------------------
import Queue
import array

# Node for Binary tree
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

# Node for AVL Tree. Inherited from Dnode
class AVLDnode(Dnode):
    __height = None
    def __init__(self, value = None, height = None, leftchild = None, rightchild = None):
        self.__height = height
        Dnode.__init__(self, value, leftchild, rightchild)

    # Get Functions
    def getheight(self):
        return self.__height

    # Set Functions
    def setheight(self, height = None):
        self.__height = height

# Node for Red Black Tree. Inherited from Dnode
class RBnode(Dnode):
    __color = None
    def __init__(self, value = None, color = None, leftchild = None, rightchild = None):
        self.__color = color
        Dnode.__init__(self, value, leftchild, rightchild)

    #Get Function
    def getcolor(self):
        return self.__color

    #Set Function
    def setcolor(self, color= None):
        self.__color = color

# Basic Node for Trie
class Tnode():
    __isend = None
    __chidren = None

    def __init__(self, chidren = 26, end = False):
        self.__chidren = [None]* chidren
        self.__isend = end

    def getisend(self):
        return self.__isend

    def setisend(self, end = False):
        self.__isend = end

    def setchildren(self, node = None, child = None):
        self.__chidren[child] = node

    def getchildren(self, child = None):
        return self.__chidren[child]

# Class to display tree values
class display:
    def __int__(self):
        pass

    def display(self, node= None, type = "inorder"):
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
        elif type == "levelorder":
            if node:
                Q = Queue.Queue(100)
                Q.put(node)
                while(Q.empty() == False):
                    node = Q.get()
                    print("Level order Node Value  = " + str(node.getvalue()))
                    if node.getleftchild() != None:
                        Q.put(node.getleftchild())
                    if node.getrightchild() != None:
                        Q.put(node.getrightchild())
        else:
            print("ERROR : Invalid Traversal type ")

# Class to perform rotations on binary search trees
class TreeRotations:
    def __init__(self):
        pass

    def rotateleft(self, node= None, debug = False):
        if node != None:
            newhead = node.getrightchild()
            temp = newhead.getleftchild()

            newhead.setleftchild(node)
            node.setrightchild(temp)

            if debug:
                print "__rotateleft() : New head  = " + str(newhead.getvalue())+ \
                " with new height = " + str(newhead.getheight()) + \
                " node = " + str(node.getvalue()) + \
                " with new height = " + str(node.getheight())

            return newhead

    def rotateright(self, node = None, debug = False):
        if node != None:
            newhead = node.getleftchild()
            temp = newhead.getrightchild()

            newhead.setrightchild(node)
            node.setleftchild(temp)

            if debug:
                print "__rotateright() : New head  = " + str(newhead.getvalue())+ \
                " with new height = " + str(newhead.getheight()) + \
                " node = " + str(node.getvalue()) + \
                " with new height = " + str(node.getheight())

            return newhead

#################
# In a complete binary tree. All levels are completely filled except possibly
# the last level and the last level have all the keys as left as possible.
################
class Completebinarytree:
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

    # Assuming all keys are unique
    def remove(self, node = None, key = None):
        if node == None:
            print "ERROR: Invalid Head"
            return
        if key == None:
            print "ERROR : Invalid Key"
            return
        # Create Queue
        Q = Queue.Queue(100)
        # Add head to Queue
        Q.put(node)
        while(Q.empty() == False):
            newnode = Q.get()
            if newnode.getvalue() == key:
                backup = newnode
            if newnode.getleftchild() != None:
                Q.put(newnode.getleftchild())
            if newnode.getrightchild() != None:
               Q.put(newnode.getrightchild())
        backup.setvalue(newnode.getvalue())

        # Delete the last node.
        Q.put(node)
        while(Q.empty() == False):
            out = Q.get()
            if out.getleftchild() == newnode:
                out.setleftchild(None)
                break
            else:
                Q.put(out.getleftchild())

            if out.getrightchild() == newnode:
               out.setrightchild(None)
               break
            else:
                Q.put(out.getrightchild())

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

    # Assuning All keys are unique
    def insert(self, node = None, key = None):
        if (node == None):
            node = Dnode(key)
        else:
            if(node.getvalue() > key):
                node.setleftchild(self.insert(node.getleftchild(),key))
            else:
                node.setrightchild(self.insert(node.getrightchild(),key))
        return node

    def remove(self, node = None, key = None):
        if node == None:
            return node

        if(node.getvalue() > key):
            node.setleftchild(self.remove(node.getleftchild(), key))
        elif(node.getvalue() < key):
            node.setrightchild(self.remove(node.getrightchild(), key))
        else:
            if((node.getleftchild() == None) and (node.getrightchild == None)):
                node = None
            elif((node.getleftchild() != None) and (node.getrightchild == None)):
                node = node.getleftchild()
            elif((node.getleftchild() == None) and (node.getrightchild != None)):
                node = node.getrightchild()
            else:
                pass
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

    def insert(self, node = None, key = None, debug = False):
        if node == None:
            return AVLDnode(key, 1)
        else:
            if(node.getvalue() > key):
                node.setleftchild(self.insert(node.getleftchild(),key, debug))
            elif(node.getvalue() < key):
                node.setrightchild(self.insert(node.getrightchild(),key, debug))

        if debug:
            print "Currently Operating on node = " + str(node.getvalue()) + \
            " of height = " + str(node.getheight()) + \
            " and Balance Factor not yet calculated "

        node.setheight(self.__newheight(node, debug))

        balance  = self.__getbalance(node, debug)

        if debug:
            print "Currently Operating on node = " + str(node.getvalue()) + \
            " of New height = " + str(node.getheight()) + \
            " and New Balance Factor = " + str(balance)

        nodeL = node.getleftchild()
        nodeR = node.getrightchild()

        if balance > 1:
            if key < nodeL.getvalue():
                if debug:
                    print "rotating right " + str(node.getvalue())
                return self.__rotateright(node, debug)

            elif key > nodeL.getvalue():
                if debug:
                    print "rotating left " + str(nodeL.getvalue()) \
                    + " followed with rotating right " + str(node.getvalue())
                node.setleftchild(self.__rotateleft(nodeL, debug))
                return self.__rotateright(node, debug)

        if balance < -1:
            if key > nodeR.getvalue():
                if debug:
                    print "rotating left " + str(node.getvalue())
                return self.__rotateleft(node, debug)

            elif key < nodeR.getvalue():
                if debug:
                    print "rotating right  " + str(nodeR.getvalue()) \
                    + " followed with rotating left " + str(node.getvalue())
                node.setrightchild(self.__rotateright(nodeR, debug))
                return self.__rotateleft(node, debug)

        return node

    def __rotateleft(self, node= None, debug = False):
        if node != None:
            newhead = node.getrightchild()
            temp = newhead.getleftchild()

            newhead.setleftchild(node)
            node.setrightchild(temp)

            node.setheight(self.__newheight(node, debug))
            newhead.setheight(self.__newheight(newhead, debug))

            if debug:
                print "__rotateleft() : New head  = " + str(newhead.getvalue())+ \
                " with new height = " + str(newhead.getheight()) + \
                " node = " + str(node.getvalue()) + \
                " with new height = " + str(node.getheight())

            return newhead

    def __rotateright(self, node = None, debug = False):
        if node != None:
            newhead = node.getleftchild()
            temp = newhead.getrightchild()

            newhead.setrightchild(node)
            node.setleftchild(temp)

            node.setheight(self.__newheight(node, debug))
            newhead.setheight(self.__newheight(newhead, debug))

            if debug:
                print "__rotateright() : New head  = " + str(newhead.getvalue())+ \
                " with new height = " + str(newhead.getheight()) + \
                " node = " + str(node.getvalue()) + \
                " with new height = " + str(node.getheight())

            return newhead

    # This will calculate balance of at each node after
    # addition of new node in a tree
    def __getbalance(self, node = None, debug = False):
        if node != None:
            nodeL = node.getleftchild()
            nodeR = node.getrightchild()

            if nodeL == None:
                Lheight = 0
            else:
                Lheight = nodeL.getheight()

            if nodeR == None:
                Rheight = 0
            else:
                Rheight = nodeR.getheight()

            if debug:
                print "__newheight() : left tree height = " + str(Lheight) + \
                " of left node value = " + str(nodeL.getvalue()) if nodeL else str("__newheight() : Left Node is None")
                print "__newheight() : right tree height  = " + str(Rheight) + \
                " of right node Value  = " + str(nodeR.getvalue()) if  nodeR else str(" __newheight(): Right Node is None")

            return (Lheight - Rheight)

    # This will calculate new height after addition of new node
    # or after rotation in a tree.
    def __newheight(self, node= None, debug = False):
       if node != None:
            nodeL = node.getleftchild()
            nodeR = node.getrightchild()

            if nodeL == None:
                Lheight = 0
            else:
                Lheight = nodeL.getheight()

            if nodeR == None:
                Rheight = 0
            else:
                Rheight = nodeR.getheight()

            if debug:
                print "__newheight() : left tree height = " + str(Lheight) + \
                " of left node value = " + str(nodeL.getvalue()) if nodeL else str("__newheight() : Left Node is None")
                print "__newheight() : right tree height  = " + str(Rheight) + \
                " of right node Value  = " + str(nodeR.getvalue()) if  nodeR else str(" __newheight(): Right Node is None")

            return(1 + max(Lheight, Rheight))

#################
# This is a complete binary tree. All levels are completely filled except possibly
# the last level and the last level have all the keys as left as possible.
# In Min Heap, The key at root must be minimum among all the keys in the binary heap
# In Max Heap, The key at root must be maximum among all the keys in the binary heap
################
class heapstruct:
    __arr = None
    def __init__(self):
        self.__arr = array.array("i")

    def insert(self, key = None):
        # Insert element in the end
        self.__arr.insert(len(self.__arr), key)
        # fetch the index of last element
        index = len(self.__arr) - 1
        # check and correct Min/Max heap propery if more than one element in the array
        if index > 0:
            while (index != 0 and (self.__arr[index] > self.__arr[self.parent(index)])):
                temp = self.__arr[self.parent(index)]
                self.__arr[self.parent(index)] = self.__arr[index]
                self.__arr[index] = temp
                index = self.parent(index)

    def parent(self, index= -1):
        if index >= 0:
            return (index - 1)/2

    def display(self):
        print self.__arr

################
# This is a binary search tree with following properties
# 1. the recent search element becomes the root
# 2. if the element in the search is not found than last
#    visted element becomes the root
# 3. the recent inserted element become the root
# This reduces the search time for most frequently accessed elements
#################

class splaytree:
    __head = None
    def __init__(self, node = None):
        self.__head = node
        self.rotation = TreeRotations()

    def gethead(self):
        return self.__head

    def sethead(self, node= None):
        self.__head = node

    def insert(self, node = None, key = None, debug = False):
        if key == None: # nothing to be done if key is none
            return node
        # This is the first node in the tree
        if ((node == None) and (key != None)):
            return Dnode(key)
        # This is not the first node
        if ((node != None) and (key != None)):
            node = self.__splay(node, key, debug)
            if debug:
                print "The return value from __splay() == " + str(node.getvalue())

        if node.getvalue() == key:
            return node
        else:
            newnode = Dnode(key)
            if node.getvalue() > key:
                newnode.setrightchild(node)
                newnode.setleftchild(node.getleftchild())
                node.setleftchild(None)
            else:
                newnode.setleftchild(node)
                newnode.setrightchild(node.getrightchild())
                node.setrightchild(None)
            return newnode

    def __splay(self, node= None, key = None, debug =False):
        if ((node == None) or (node.getvalue() == key)):
            return node

        if node.getvalue() > key:
            if node.getleftchild() == None:
                return node

            nodeL = node.getleftchild()

            if debug:
                print "The value of current node == " + str(node.getvalue()) + \
                " The value of left child ==" + str(nodeL.getvalue())

            if(nodeL.getvalue() > key):
                nodeL.setleftchild(self.__splay(nodeL.getleftchild(), key))
                if debug:
                    print "Right rotating in left subtree == " + str(nodeL.getvalue())
                node = self.rotation.rotateright(node)
            else:
                nodeL.setrightchild(self.__splay(nodeL.getrightchild(), key))
                if nodeL.getrightchild() != None:
                    if debug:
                        print "left rotating in left subtree(when right child is not NULL) == " \
                        + str(nodeL.getvalue())
                    node = self.rotation.rotateleft(node)

            if debug:
                print "Head Node after one rotation in left subtree == " + str(node.getvalue())

            if nodeL.getleftchild() == None:
                return node
            else:
                return self.rotation.rotateright(node)

        else:
            if node.getrightchild() == None:
                return node

            nodeR = node.getrightchild()

            if debug:
                print "The value of current node == " + str(node.getvalue()) + \
                " The value of right child ==" + str(nodeR.getvalue()) + \
                "  The key valye paased in == " + str(key)

            if nodeR.getvalue() > key:
                nodeR.setrightchild(self.__splay(nodeR.getrightchild(), key))
                if nodeR.getleftchild() != None:
                    if debug:
                        print "right rotating in right subtree(when left child is not NULL) == " \
                        + str(nodeR.getvalue())
                    node = self.rotation.rotateright(node)
            else:
                nodeR.setrightchild(self.__splay(nodeR.getrightchild(), key))
                if debug:
                    print "Left rotating in Right subtree == " + str(nodeR.getvalue())
                node = self.rotation.rotateleft(node)

            if debug:
                print "Head Node after one rotation in right subtree == " + str(node.getvalue())

            if nodeR.getrightchild() == None:
                return node
            else:
                return self.rotation.rotateleft(node)
############
# This is a tree that store strings.
# Maximum number of children of a node is equal to size of alphabet.
# Trie supports search, insert and delete operations in O(L) time where L is length of key.
############
class triestruct:
    __head = None
    def __init__(self, node = None):
        self.__head = Tnode()

    def gethead(self):
        return self.__head

    def sethead(self, node= None):
        self.__head = node

    def insert(self, node = None, word= None):
        # head is none
        if node == None :
            return False
        # Word is none
        if ((node != None) and (word == None)):
            return False

        # get the length of word
        length = len(word)

        # Traverse charcter by charcter and insert
        for val in range(length):
            index = self.__getindex(word[val])
            if node.getchildren(index) == None:
                node.setchildren(Tnode(), index)
                node = node.getchildren(index)
            node.setisend(True)

        return True

    def search(self, node = None, word = None):
         # head is none
        if node == None :
            return False
        # Word is none
        if ((node != None) and (word == None)):
            return False

        # get the length of word
        length = len(word)

         # Traverse charcter by charcter and insert
        for val in range(length):
            index = self.__getindex(word[val])
            if node.getchildren(index) == None:
                return False
            else:
                node = node.getchildren(index)

        return node.getisend()

    def __getindex(self, char = None):
        char = char.lower()
        return(ord(char) - 97)

##################
# This is another self balancing Binary Search Tree with following properties
# 1. Every Node has a color. either red or black
# 2. Root is always black
# 3. There are no two adjacent red nodes. (A red node cannot have a red parent or child)
# 4. Every Path from Root to its descendant NULL have the same umber of black node.
##################
class redblacktree:
    __head = None
    def __init__(self, node = None):
        self.__head = node

    def gethead(self):
        return self.__head

    def sethead(self, node= None):
        self.__head = node

    def insert(self, node = None, key = None, debug = False):
        pass

class suffixtree:
    __head = None
    def __init__(self, node = None):
        self.__head = node

    def gethead(self):
        return self.__head

    def sethead(self, node= None):
        self.__head = node

class huffmantree:
    __head = None
    def __init__(self, node = None):
        self.__head = node

    def gethead(self):
        return self.__head

    def sethead(self, node= None):
        self.__head = node

########
# This class is created to test various tree structures.
########
class testcases:
    def __init__(self):
        self.disp = display()

    def TC_binarysearchtree(self):
        print "********* START: Binary Search Tree Test cases ****************"
        # Create Instance Of Binary Search Tree Class
        bst = binarysearchtree()
        # Generating Binary Search Tree by inserting element by element
        bst.sethead(bst.insert(bst.gethead(),50))
        bst.sethead(bst.insert(bst.gethead(),30))
        bst.sethead(bst.insert(bst.gethead(),70))
        bst.sethead(bst.insert(bst.gethead(),20))
        bst.sethead(bst.insert(bst.gethead(),10))
        # Display Binary Search Tree
        self.disp.display(bst.gethead(), "preorder")
        print "********* END: Binary Search Tree Test cases ****************"

    def TC_binarytree(self):
        print "********* START: Complete Binary Tree Test cases ****************"
        #create instance of binary tree
        btree = Completebinarytree()
        # Generate Binary Tree by inserting element by element
        btree.sethead(btree.insert(btree.gethead(), 50))
        btree.sethead(btree.insert(btree.gethead(), 60))
        btree.sethead(btree.insert(btree.gethead(), 70))
        btree.sethead(btree.insert(btree.gethead(), 30))
        btree.sethead(btree.insert(btree.gethead(), 40))
        btree.sethead(btree.insert(btree.gethead(), 10))

        # Display Binary Tree
        self.disp.display(btree.gethead(), "levelorder")
        print "------------------------------------"

        # Remove Elements
        btree.remove(btree.gethead(), 10)
        self.disp.display(btree.gethead(), "levelorder")
        print "------------------------------------"
        btree.remove(btree.gethead(), 50)
        self.disp.display(btree.gethead(), "levelorder")
        print "------------------------------------"
        btree.remove(btree.gethead(), 30)
        self.disp.display(btree.gethead(), "levelorder")
        print "------------------------------------"
        print "********* END: Complete Binary Tree Test cases ****************"

    def TC_AVLtree(self):
        print "********* START: AVL Tree Test cases ****************"
        # Create Instance of AVL Tree Class
        AVLtree = avltree()
        # Insert Elements
        AVLtree.sethead(AVLtree.insert(AVLtree.gethead(), 50, False))
        AVLtree.sethead(AVLtree.insert(AVLtree.gethead(), 30, False))
        AVLtree.sethead(AVLtree.insert(AVLtree.gethead(), 70, False))
        AVLtree.sethead(AVLtree.insert(AVLtree.gethead(), 20, False))
        AVLtree.sethead(AVLtree.insert(AVLtree.gethead(), 10, False))
        AVLtree.sethead(AVLtree.insert(AVLtree.gethead(), 40, False))
        AVLtree.sethead(AVLtree.insert(AVLtree.gethead(), 100, False))
        AVLtree.sethead(AVLtree.insert(AVLtree.gethead(), 150, False))
        # Display AVL Tree
        self.disp.display(AVLtree.gethead(), "preorder")
        # Display AVL Tree
        self.disp.display(AVLtree.gethead(), "inorder")
        print "********* END: AVL Tree Test cases ****************"

    def TC_Binaryheap(self):
        print "********* START: Binary Heap Test cases ****************"
        #Create Instance of Binary Heap
        bheap = heapstruct()
        # Insert Elements
        bheap.insert(10)
        bheap.insert(20)
        bheap.insert(15)
        bheap.insert(18)
        bheap.insert(16)
        bheap.insert(30)
        bheap.insert(25)
        # Display Element
        bheap.display()
        print "********* END: Binary Heap Test cases ****************"

    def TC_splaytree(self):
        print "********* START: splay Tree Test cases ****************"
        # Create Instance of Splay tree
        stree = splaytree()
        # insert Element
        stree.sethead(stree.insert(stree.gethead(), 100, False))
        stree.sethead(stree.insert(stree.gethead(), 50, False))
        stree.sethead(stree.insert(stree.gethead(), 150, False))
        stree.sethead(stree.insert(stree.gethead(), 120, False))
        stree.sethead(stree.insert(stree.gethead(), 110, False))
         # Display Splay  Tree
        self.disp.display(stree.gethead(), "preorder")
        print "********* END: splay Tree Test cases ******************"

    def TC_triestruct(self):
        print "********* START: Tries Tree Test cases ****************"
        trie = triestruct()
        # Insert Words
        trie.insert(trie.gethead(), "hello")
        trie.insert(trie.gethead(), "world")
        trie.insert(trie.gethead(), "This")
        trie.insert(trie.gethead(), "is")
        trie.insert(trie.gethead(), "Prabhjeet")
        # Search Words
        print trie.search(trie.gethead(),"hello")
        print trie.search(trie.gethead(),"world")
        print trie.search(trie.gethead(),"this")
        print trie.search(trie.gethead(),"is")
        print trie.search(trie.gethead(),"ishu")
        print trie.search(trie.gethead(),"prabhjeet")

        print "********* END: Tries Tree Test cases ****************"

    def TC_redblacktree(self):
        print "********* START: Red Black Tree Test cases ****************"
        print "********* END: Red Black Tree Test cases ****************"

    def TC_suffixtree(self):
        print "********* START: siffix Tree Test cases ****************"
        print "********* END: siffix Tree Test cases ****************"

    def TC_huffmantree(self):
        print "********* START: huffman Tree Test cases ****************"
        print "********* END: huffman Tree Test cases ****************"

def main():
    tc = testcases()
    tc.TC_binarytree()
    tc.TC_binarysearchtree()
    tc.TC_AVLtree()
    tc.TC_Binaryheap()
    tc.TC_splaytree()
    tc.TC_triestruct()
    tc.TC_redblacktree()
    tc.TC_suffixtree()
    tc.TC_huffmantree()

if __name__ == '__main__':
    main()
