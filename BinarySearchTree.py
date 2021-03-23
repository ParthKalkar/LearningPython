print("Welcome to the Binary Search Tree and some of its features!!!")
class Node: 
  
    
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
  
  

def postorder(root):
    if root is not None:
        postorder(root.left) 
        postorder(root.right)
        print(root.key)

def preorder(root):
    if root is not None:
        print(root.key)
        preorder(root.left) 
        preorder(root.right)

def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print(root.key) 
        inorder(root.right) 
  
  

def insert( node, key): 
  
    
    if node is None: 
        return Node(key) 
  
    
    if key < node.key: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
  
    
    return node 
  

def minValueNode(node): 
    current = node 
  
    
    while(current.left is not None): 
        current = current.left  
  
    return current  
  

def deleteNode(root, key): 
  
   
    if root is None: 
        return root  
  
    if key < root.key: 
        root.left = deleteNode(root.left, key) 
  
    elif key > root.key: 
        root.right = deleteNode(root.right , temp.key) 
    else:
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        temp = minValueNode(root.right) 
  
        
        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)
    return root
root = None
while True:
    if input("Enter either of Y or y to continue: ").upper()!='Y':
     break    
    c=int(input("Enter the integer input to be inserted: "))
    root = insert(root, c) 

  
print ("Inorder traversal of the given tree is as follows; ")
inorder(root) 

while True:
    if input("Enter either of Y or y: ").upper()!='Y':
     break    
    c=int(input("Enter the integer input to be deleted: "))
    print ("\nDelete",c)
    root = deleteNode(root, c)
    print ("Inorder traversal of the modified tree is as follows; ")
    inorder(root)

print("As we have multiple traversing methods for a tree, we have choices to go with!")
choose=int(input("Press 1 for PreOrder, 2 for PostOrder and 3 for InOrder: "))
if choose == 1:
    print("Well congratualations, you have chosen to traverse the tree by PreOrder method i.e NLR!")
    print("PreOrder traversal of the modified tree is as follows; ")
    preorder(root)
elif choose == 2:
    print("Well congratualations, you have chosen to traverse the tree by PostOrder method i.e LRN!")
    print("PostOrder traversal of the modified tree is as follows; ")
    postorder(root)
else:
    print("Well, you have not chosen anyone of the above two methods to traverse the tree, Hence InOrder method i.e LNR!")
    print("InOrder traversal of the modified tree is as follows; ")
    inorder(root)
    
    
    
    
  


