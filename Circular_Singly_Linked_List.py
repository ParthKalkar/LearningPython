class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head.next
        print(self.head.data)
        while printval is not self.head:
            print(printval.data)
            printval = printval.next

    def AtFront(self, newdata):

        NewNode = Node(newdata)
        NewNode.next = self.head

        if self.head == None:
            self.head = NewNode
            NewNode.next = self.head
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            NewNode.next = self.head
            ptr.next = NewNode
            self.head = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        NewNode.next = self.head
        ptr.next = NewNode

    def AfterValue(self,value,val):
        NewNode = Node(newdata)
        NewNode.next = self.head
        ptr = self.head
        while ptr.data != value:
            ptr = ptr.next
        NewNode.next = ptr.next
        ptr.next = NewNode

    def DelAtEnd(self):
        if self.head == None:
            print("Underflow")
            return
        ptr=self.head
        preptr = self.head
        while ptr.next != self.head:
            preptr = ptr
            ptr = ptr.next
        preptr.next = self.head

    def DelAtFront(self):
        if self.head == None:
            print("Underflow")
            return
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        ptr = self.head.next
        self.head = self.head.next

    def DelAfterValue(self,value):
        if self.head == None:
            print("Underflow")
            return
        ptr = self.head
        preptr = self.head
        while ptr.data != value:
            preptr = ptr
            ptr = ptr.next
        preptr.next = ptr.next

CLL = CSLL()
CLL.AtFront("Mon")
CLL.AtFront("Tue")
CLL.AtFront("Wed")
CLL.AtFront("Thu")
CLL.AtEnd("Tue")
CLL.DelAtEnd()
CLL.listprint()            


        
