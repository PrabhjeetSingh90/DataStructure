#-------------------------------------------------------------------------------
#
# Author:      prabhjeet Singh
#
# Purpose : The Purpose of the code is to implement the software cache
#           Here are some of the assumptions taken:
#           1. The memory is limited and size is provided by command line argument
#           2. The algorithm used to evict the element is LRU(Least Recently Used)
#
#-------------------------------------------------------------------------------
class Dnode:
    def __init__(self, key = None, value = None, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    def getkey(self):
        return self.key
    def getvalue(self):
        return self.value
    def getleft(self):
        return self.left
    def getright(self):
        return self.right

class cache:
    __size = 0
    def __init__(self, size = 0):
        self.__size = size
        self.head = None
        self.tail = None
        self.map = dict()

    def add(self, key = 0, value = 0):
        if True == self.map.has_key(key):
            # Value already present in List.
            # Just move it to beginning to ensure lease recently used
            print self.map[key]
            self.__Shift_first(self.map[key])
        else:
            new = Dnode(key, value)
            mapsize = len(self.map)
            # Cache is full. Delete the old entry and add new one
            if mapsize >= int(self.__size):
                lastkey = self.__Del_Last()
                print "The value of last key = " + str(lastkey)
                del self.map[lastkey]
                self.map[key] = new
                self.__add_first(new)
            else: # Cache still have space to accomodate new entry
                self.map[key] = new
                self.__add_first(new)

    # Adding front of doubly linked list with new node as input
    def __add_first(self, node = None):
        if self.head == None: # Adding First node into List
            self.head = node
            self.tail = node
        else: # Adding new node in the front
            node.right = self.head
            self.head.left = node
            self.head = node

    # Deleting the last element of double linked list and return the key from node.
    def __Del_Last(self):
        if self.tail != None: # Ensure List is Not Empty
            key = self.tail.getkey() # Get the key from last recently used Node
            self.tail = self.tail.getleft() # Update the tail to new tail Value
            self.tail.right = None # set the tail right = None to break the link
            return key

    def __Shift_first(self, node=None):
        leftnode = node.getleft()
        rightnode = node.getright()
        print leftnode
        print rightnode

        if leftnode == None: # Already a front Node. No need to modify
            pass
        elif rightnode == None: # This is the last node.
            # Update the tail
            self.tail = leftnode
            leftnode.right = None

            # Shift the node to front
            node.left = None
            node.right = self.head
            self.head = node
        else: # This is middle node
            # Break the links of existing node
            leftnode.right = rightnode
            rightnode.left = leftnode

            # Shift the node to front / Links are broken
            node.left = None
            node.right = self.head
            self.head = node

    # Function to display current Map and List value
    def display(self):
        # Print the current map value
        print self.map
        # Print the Current list value
        current = self.head
        while current:
            print "Node key = " + str(current.getkey()) + " Value = " + str(current.getvalue())
            current = current.getright()

def main():
    size = raw_input("Enter the Size of cache to be: ")

    # Chache Operations.
    # Currently we are uniquely assigning key to each data
    # However unique key can be generated from data using good hash function
    #
    x =cache(size)
    x.add(1, 10)
    x.display()
    x.add(2, 20)
    x.display()
    x.add(3, 30)
    x.display()
    x.add(2, 20)
    x.display()
    x.add(2, 20)
    x.display()
    x.add(4, 40)
    x.display()
    x.add(5, 50)
    x.display()
    x.add(4, 40)
    x.display()
    x.add(5, 50)
    x.display()
    #x.add(6, 60)
    #x.display()

if __name__ == '__main__':
    main()
