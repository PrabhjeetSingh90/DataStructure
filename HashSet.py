#-------------------------------------------------------------------------------
#
# Author:      prabhjeet Singh
#
# Purpose : Demonstration of hashset implemetation.
#
#-------------------------------------------------------------------------------
from array import *

class Snode:
    def __init__(self, data = None, right = None):
        self.data = data
        self.right = right
    def getdata(self):
        return self.data
    def getright(self):
        return self.right

class bucket:
    __arr = list()
    __Size = 0

    def __init__(self, val=20):
        for x in range(val):
            self.__arr.append(None)
        self.__Size = val

    def TraverseBucket(self):
       for x in range(self.__Size):
            if(self.__arr[x] != 0):
                temp = self.__arr[x]
                while(temp):
                    print "bucket = " + str(x) + " Value = " + str(temp.getdata())
                    temp = temp.getright()

    def getsize(self):
        return self.__Size

    def insertelement(self, key, data):
        if (self.__arr[key] == None):
            new = Snode(data)
            new.right = None
            self.__arr[key] = new
        else:
            temp = self.__arr[key]
            while(temp.getright() != None):
                temp = temp.getright()
            new = Snode(data)
            temp.right = new
        print self.__arr

    def fetchelement(self,key, data):
        temp = self.__arr[key]
        ret = None
        if temp != None:
            if (temp.getdata() == data):
                if temp.getright != None:
                    self.__arr[key] = temp.getright()
                else:
                    self.__arr.insert(key,0)
            else:
                while(temp.getdata() != data):
                    prev = temp
                    temp = temp.getright()
                prev.right = temp.getright()
                ret = data
        print self.__arr
        return ret

class hashset_list:
    def __init__(self):
        print"calling hashset"
        self.hsh = bucket()

    def put(self,data):
        key = self.generatehashkey(data)
        self.hsh.insertelement(key, data)

    def get(self, data):
        key = self.generatehashkey(data)
        op = self.hsh.fetchelement(key, data)
        return op

    def generatehashkey(self, data):
        key = data%(self.hsh.getsize())
        return key

    def TraverseHash(self):
        self.hsh.TraverseBucket()

def main():
    hset = hashset_list()
    hset.put(10)
    hset.put(30)
    hset.put(50)
    hset.TraverseHash()
    hset.get(10)
    hset.TraverseHash()
    hset.get(30)
    hset.TraverseHash()
    hset.get(50)
    hset.TraverseHash()
    pass


if __name__ == '__main__':
    main()
