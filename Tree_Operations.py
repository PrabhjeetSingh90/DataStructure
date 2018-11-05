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


class binarytree:
    pass

class binarysearchtree:
    pass

class avltree:
    pass

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

def main():
    pass

if __name__ == '__main__':
    main()
