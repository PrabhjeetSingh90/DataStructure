#-------------------------------------------------------------------------------
#
# Author:      prabhjeet Singh
#
# Purpose : Implementation of Linked List Operations
#
#-------------------------------------------------------------------------------

class node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def setleft(self, new_left):
        self.left = new_left
    def setright(self, new_right):
        self.right = new_right

class Doublylinkedlist:
    def __init__(self, head=None):
        self.head=head
    # Add node at front
    def addfront(self, data):
        new_node = node(data)
        if(self.head == None):
            self.head = new_node
            new_node.left = None
            new_node.right = None
        else:
            new_node.left = None
            new_node.right = self.head
            self.head.left = new_node
            self.head = new_node
    # Add node at End
    def addend(self, data):
        new_node = node(data)
        if(self.head == None):
            self.head = new_node
            new_node.setleft = None
            new_node.setright = None
        else:
            current = self.head
            while current.getright() != None:
                current = current.getright()
            current.right = new_node
            new_node.left = current
            new_node.right = None
    # Add node at Specified Index
    def addatindex(self, data, index):
        if index == 1:
            self.addfront(data)
        else:
            current = self.head
            count = 0
            while current:
                count = count + 1
                current = current.getright()
            if index == count+1:
                self.addend(data)
            if index < count:
                new_node = node(data)
                current = self.head
                count = 1
                while count != index:
                    count = count + 1
                    Previousnode = current
                    current = current.getright()
                new_node.right = current
                new_node.left = current.left
                current.left = new_node
                Previousnode.right = new_node
    # print the current list
    def traverse(self):
        current = self.head
        if current == None:
            pass
        else:
            while current:
                print current.getdata()
                current = current.getright()
    #Delete the front Node
    def delfront(self):
        self.head = self.head.getright()
        self.head.left = None
    # Delete the last node
    def delend(self):
        current = self.head
        while  current.getright() != None:
            previous = current
            current = current.getright()
        previous.right = None
    # Delete node Specified by Index
    def delatindex(self, index):
        if index == 1:
            self.delfront()
        else:
            current = self.head
            count = 0
            while current:
                count = count + 1
                current = current.getright()
            if index == count+1:
                self.delend()
            if index < count:
                current = self.head
                count = 1
                while count != index:
                    count = count + 1
                    prevnode = current
                    current = current.getright()
                    nextnode = current.getright()
                prevnode.right = nextnode
                nextnode.left = prevnode
def main():
    # Create the list
    list = Doublylinkedlist()
    # Add in front of list
    list.addfront(10)
    list.addfront(20)
    list.addfront(30)
    # Print the list
    print"Traversal 1"
    list.traverse()
    # Add at the end of list
    list.addend(40)
    list.addend(50)
    list.addend(60)
    # Print the list
    print "Traversal 2"
    list.traverse()
    list.addatindex(101, 1)
    list.addatindex(201, 8)
    list.addatindex(301, 2)
    list.addatindex(401, 9)
    list.addatindex(501, 5)
    print "Traversal 3"
    list.traverse()
    list.delatindex(3)
    list.delatindex(5)
    list.delatindex(2)
    print "Traversal 4"
    list.traverse()
    list.delfront()
    list.delfront()
    list.delfront()
    print "Traversal 5"
    list.traverse()
    list.delend()
    list.delend()
    list.delend()
    print "Traversal 6"
    list.traverse()


if __name__ == '__main__':
    main()
