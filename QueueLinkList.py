import LinkList

class Queue(LinkList.LinkList):

    def showqueue(self):
        self.showlist()

    def enqueue(self,data):
        self.addattail(data)

    def dequeue(self):
        print self.Head.get_data(),"is the dequeued data"
        print "Rest of the Queue:"
        self.delhead()

def main():
    pass

if __name__ == '__main__':
    main()

    Queuell = Queue()
    Queuell.enqueue(10)
    Queuell.enqueue(20)
    Queuell.enqueue(45)
    Queuell.showqueue()
    Queuell.dequeue()
    Queuell.showqueue()
