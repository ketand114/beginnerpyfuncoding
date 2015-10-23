class Node(object):
    #define node in the list
    def __init__(self, data, nextnode):
        self.data = data
        self.nextnode = nextnode
    def get_data(self):
        return self.data
    def get_next(self):
        return self.nextnode
    def set_next(self,new_next):
        self.nextnode = new_next


class LinkList(object):
    Head = None
    Tail = None

    def addathead(self,data):
        newNode = Node(data,None)
        if self.Head == None:
            self.Head = self.Tail = newNode
        else:
            newNode.set_next(self.Head)
            self.Head = newNode

    def addattail(self,data):
        newNode = Node(data,None)
        if self.Head == None:
            self.Head = self.Tail = newNode
        else:
            self.Tail.set_next(newNode)
            self.Tail = newNode


    def delhead(self):
        if self.Head == None:
            print "No Nodes to delete"
        elif self.Head == self.Tail:
            NodetoDel = self.Head
            self.Head = self.Tail=None
            del NodetoDel
        else:
            NodetoDel = self.Head
            self.Head = NodetoDel.get_next()
            del NodetoDel


    def deltail(self):
        if self.Tail == None:
            print "No Nodes to delete"
        elif self.Head == self.Tail:
            self.Head = None
            self.Tail = None
        else:
            NodetoDel = self.Tail
            currNode = self.Head
            while currNode.get_next() is not NodetoDel:
                currNode = currNode.get_next()
            currNode.set_next(None)
            self.Tail = currNode


    def delnode(self,del_data):
        if self.Head == None:
            print "No nodes to delete"
        else:
            currNode = self.Head
            prevNode = None
            while currNode is not None:
                if currNode.get_data() == del_data:
                    if prevNode == None:
                        self.Head = currNode.getnext()
                    else:
                        prevNode.set_next(currNode.get_next())
                prevNode = currNode
                currNode = currNode.get_next()


    def showlist(self):
        if self.Head == None:
            print "No data in list"
        else:
            CurrentNode = self.Head
            while CurrentNode is not None:
                print CurrentNode.get_data(),"->",
                CurrentNode = CurrentNode.get_next()
            print None
