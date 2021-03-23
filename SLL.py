class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
		
    def RemoveNode(self, Removekey):

        Head = self.head

        if (Head is not None):
            if (Head.data == Removekey):
                self.head = Head.next
                Head = None
                return

        while (Head is not None):
            if Head.data == Removekey:
                break
            prev = Head
            Head = Head.next

        if (Head == None):
            return

        prev.next = Head.next
        Head = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()            
