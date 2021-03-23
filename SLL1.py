class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

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
        self.head = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is not present")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode   



L1 = SLinkedList()

ans = "Y"
while ans == "Y" or ans == "y":
    choose = int(input("Enter 1 for Insertion at beginning, 2 for Insertion at end and 3 for Insertion in between the node: "))
    
    if choose == 1:
        print("You have choosen to insert the element at the front")
        n = int(input("Enter the number of nodes you want in your singly linked list: "))
        for i in range(n):
            i = input("Enter something in the singly linked list: ")
            L1.AtBegining(i)

    elif choose == 2:
        print("You have choosen to insert the element at the end")
        n = int(input("Enter the number of nodes you want in your singly linked list: "))
        for i in range(n):
            i = input("Enter something in the singly linked list: ")
            L1.AtEnd(i)
    else :
        print("You have choosen to insert the element in between the node")
        n = int(input("Enter the number of nodes you want in your singly linked list: "))
        for i in range(n):
            i = input("Enter something in the singly linked list: ")
            L1.Inbetween(i)
    ans = input("Press Y or y to continue: ")


L1.listprint()
