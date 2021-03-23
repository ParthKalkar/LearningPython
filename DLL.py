class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        ptr = self.head
        if self.head is None:
            self.head = NewNode
            return
        ptr.prev = NewNode
        self.head = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode
        NewNode.prev = last

    def AfterValue(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is not present")
            return

        NewNode = Node(newdata)
        NewNode.next = None
        NewNode.prev = None

llist = SLinkedList()
llist.AtBegining("Mon")
llist.AtBegining("Tue")
llist.AtBegining("Wed")
llist.AtEnd("Mon")
llist.AtEnd("Tue")
llist.AtEnd("Wed")
llist.listprint()   
