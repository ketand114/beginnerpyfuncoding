import LinkList

class Stack(LinkList.LinkList):

    def showstack(self):
        self.showlist()

    def push(self,data):
        self.addathead(data)

    def pop(self):
#        print self.Head.get_data(),"---data popped from stack--"
#        print "Rest of the Stack:"
        data = self.Head.get_data()
        self.delhead()
        return data


#def main():
#    pass

#if __name__ == '__main__':
#    main()

#    Stackll = Stack()
#    Stackll.push(10)
#    Stackll.push(20)
#    Stackll.push(45)
#    Stackll.showstack()
#    data =  Stackll.pop()
#    print data,"---data popped from stack--"
#    Stackll.showstack()
