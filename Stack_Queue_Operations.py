#-------------------------------------------------------------------------------
#
# Author:      prabhjeet Singh
#
# Pupose : Implementation of Stack and Queue operations using linked list
#
#-------------------------------------------------------------------------------

class Dnode:
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

class Snode:
    def __init__(self, data = None, right = None):
        self.data = data
        self.right = right
    def getdata(self):
        return self.data
    def getright(self):
        return self.right

class stack:
    def __init__(self, head=None):
        self.head=head
    # Add node at front

    def push(self,data):
        new = Snode(data)
        if(self.head == None):
            new.right = None
            self.head = new
        else:
            new.right = self.head
            self.head= new

    def pop(self):
        data = None
        if(self.head != None):
            data = self.head.getdata()
            self.head = self.head.getright()
        return data

class queue:
    def __init__(self, head=None, tail = None):
        self.head = head
        self.tail = tail

    def push(self,data):
        new = Dnode(data)
        if self.head == None:
            new.right = None
            new.left = None
            self.head = new
            self.tail = new
        else:
            self.head.left = new
            new.right = self.head
            new.left = None
            self.head = new

    def pop(self):
        data = None
        if(self.tail != None):
            data = self.tail.getdata()
            self.tail = self.tail.getleft()
        return data

def main():
    # Create stack and Queue
    stk = stack()
    q = queue()

    stk.push(10) # Push Element 1 into stack
    stk.push(100) # Push Element 2 into stack
    # Pop all Elements from Stack
    print "Pop operation 1 form stack ="  + str(stk.pop())
    print "Pop operation 2 form stack ="  + str(stk.pop())
    print "Pop operation 3 form stack ="  + str(stk.pop())
    print "Pop operation 4 form stack ="  + str(stk.pop())

    q.push(201) # Push Element 1 into Queue
    q.push(301) # Push Element 2 into Queue
    # pop all Elements from Queue
    print "Pop operation 1 form Queue ="  + str(q.pop())
    print "Pop operation 2 form Queue ="  + str(q.pop())
    print "Pop operation 3 form Queue ="  + str(q.pop())
    print "Pop operation 4 form Queue ="  + str(q.pop())

if __name__ == '__main__':
    main()
