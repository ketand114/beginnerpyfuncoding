class QuArray(object):
    head = None
    tail = None
    Quearray = [None]*1

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get_array(self):
        return self.Quearray

    def set_head(self,newhead):
        self.head = newhead

    def set_tail(self,newtail):
        self.tail = newtail

    def set_array(self,newarray):
        self.Quearray = newarray

    def set_arrayelem(self,position,data):
        self.Quearray[position]=data

    def get_arrayelem(self,position):
        return self.Quearray[position]

    def get_quelen(self):
        h = self.get_head()
        t = self.get_tail()
        l = len(self.get_array())
        if h<t:
            return (t-h)+1
        elif t<h:
            return (l-h)+t+1
        else:
            if h is None and t is None:
                return 0
            else:
                return 1

    def isqueueEmpty(self):
        if self.get_quelen() < len(self.get_array()):
            return True
        else:
            return False

    def showqueue(self):
        for i in range(len(self.Quearray)):
            print "|", self.Quearray[i],
        print "|"
        print "Head:",self.get_head(),"  Tail:",self.get_tail()

    def enqueue(self,data):
        if self.get_head() is None and self.get_tail() is None:
            self.set_arrayelem(0,data)
            self.set_head(0)
            self.set_tail(0)
        else:
            if not self.isqueueEmpty():
                self.resizeup()
            t=self.get_tail()
            if t is None:
                t = 0
            newtail = t + 1
            alen = len(self.get_array())
            if newtail >= alen:
                newtail = newtail-alen
            self.set_arrayelem(newtail,data)
            self.set_tail(newtail)

    def dequeue(self):
        qlen = self.get_quelen()
        alen = len(self.get_array())
        h = self.get_head()
        t = self.get_tail()
        if h == None and t == None:
            print "No data in Queue"
        elif qlen-1 > (alen/4):
            print "Element dequeued is:",self.get_arrayelem(h)
            self.set_arrayelem(h,None)
            if h+1<alen:
                self.set_head(h+1)
            else:
                self.set_head((h+1)-alen)
        elif qlen==1:
            print "Element dequeued is:",self.get_arrayelem(h)
            self.set_arrayelem(h,None)
            self.set_head(None)
            self.set_tail(None)
        else:
            if qlen-1<=(alen/4):
                print "Element dequeued is:",self.get_arrayelem(h)
                self.set_arrayelem(h,None)
                if h+1<alen:
                    self.set_head(h+1)
                else:
                    self.set_head((h+1)-alen)
                self.resizedown()



    def resizeup(self):
        head = self.get_head()
        tail = self.get_tail()
        array = self.get_array()
        newarray = [None]*(len(array)*2)
        i=0
        if head <= tail:
            for j in range(head,tail+1):
                newarray[i] = array[j]
                i=i+1
        else:
            for j in range(head,len(array)):
                newarray[i] = array[j]
                i=i+1
            for j in range(0,tail+1):
                 newarray[i]=array[j]
                 i=i+1
        self.set_head(0)
        self.set_tail(i-1)
        self.set_array(newarray)


    def resizedown(self):
        head = self.get_head()
        tail = self.get_tail()
        array = self.get_array()
        newarray = [None]*(len(array)/2)
        if head is None and tail is None:
            self.set_head(None)
            self.set_tail(None)
            self.set_array(newarray)
        else:
            i=0
            if head <= tail:
                for j in range(head,tail+1):
                    newarray[i] = array[j]
                    i=i+1
            else:
                for j in range(head,len(array)):
                    newarray[i] = array[j]
                    i=i+1
                for j in range(0,tail+1):
                    newarray[i]=array[j]
                    i=i+1
            self.set_head(0)
            self.set_tail(i-1)
            self.set_array(newarray)



def main():
    pass

if __name__ == '__main__':
    main()

    Queuell = QuArray()
    Queuell.enqueue(10)
    Queuell.showqueue()
    Queuell.enqueue(20)
    Queuell.enqueue(45)
    Queuell.showqueue()
    Queuell.dequeue()
    Queuell.showqueue()
    Queuell.enqueue(90)
    Queuell.showqueue()
    Queuell.dequeue()
    Queuell.showqueue()
    Queuell.enqueue(30)
    Queuell.showqueue()
    Queuell.enqueue(10)
    Queuell.showqueue()
    Queuell.enqueue(20)
    Queuell.showqueue()
    Queuell.dequeue()
    Queuell.dequeue()
    Queuell.dequeue()
    Queuell.dequeue()
    Queuell.showqueue()
    Queuell.dequeue()
    Queuell.showqueue()
