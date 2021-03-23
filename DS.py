print("Welcome to the world of arrays , We can perform various operations on the array \n Some of the operations are: Insertion and Deletion")
def INSERT_END (arr, size, n, data) :
	if n == 0 :
		arr[0] = data
		n = n+1
		return arr[0]
	elif n < size :
		arr[n] = data
		n = n+1
		return arr[0]
def INSERT_FRONT (arr, size, n, data) :
	if n == 0 :
		arr[0] = data
		n = n+1
		return
	elif n < size :
		i = n-1
		while i >= 0 :
			arr[i+1] = arr[i]
			i = i-1
		arr[0] = data
		n = n+1
		return 
def INSERT_POSITION (arr, size, n, data ,LOC) :
	LOC = int(input("Enter the location you want to insert :"))
	if n == 0 :
		arr[0] = data
	elif n > 0 and LOC < n :
		i = LOC + 1
		while i <= n :
			arr[i-1] = arr[i]
			i = i+1
		n = n+1
		return arr[LOC]
def DELETE_POSITION (arr, size, n) :
	LOC = int(input("Enter the location you want to delete :"))
	if n == 0 :
		print("No element to delete")
	elif n > 0 and LOC < n :
		arr[LOC] = None
		i = LOC + 1 
		while i <= n :
			arr[i-1] = arr[i]
			i = i+1
		arr[n-1] = None
		n = n -1
		return
def DELETE_END (arr, size, n) :
	if n == 0 :
		print("No element to delete")
		return
	elif n < size :
		print("The deleted value is :" , arr[n-1])
		arr[n-1] = None
		n = n-1
		return 
def DELETE_FRONT (arr, size, n) :
	if n == 0 :
		print("No element to delete")
		return
	elif n < size :
		i = n-1
		while i >= 0 :
			arr[i+1] = arr[i]
			i = i-1
		arr[0] = None
		n = n-1
		return
size = int(input("Enter the desired size of the array : "))
arr = [None]*size
n = int(input("Insert the number of elements currently present in the array : "))
data = input("Enter the data you want to insert : ")
choose = int(input("Choose either of 1 for Insertion or 2 for Deletion : "))
if choose == 1 :
	print("What type of Insertion do you want to perform ?")
	insert_type = int(input("Choose a type of Insertion : 1 for At_End , 2 for At_Front and 3 for At_Position")) 
	if insert_type == 1 :
		print("You have choosen to insert the element at the end")
		new1 = INSERT_END(arr, size, n, data)
		print(new1)
	elif insert_type == 2 :
		print("You have choosen to insert the element at the front")
		new2 = INSERT_FRONT(arr, size, n, data)
		print(new2)
	elif insert_type == 3 :
		print("You have choosen to insert the element at the given position")
		new6 = INSERT_POSITION (arr, size, n, data ,LOC) 
		print(new6)	
elif choose == 2 :
	print("What type of Deletion do you want to perform ?")
	delete_type = int(input("Choose a type of Deletion : 1 for At_End , 2 for At_Front and 3 for At_Position"))
	if delete_type == 1 :
		print("You have choosen to delete the element at the end")	
		new3 = DELETE_END(arr, size, n)
		print(new3)
	elif delete_type == 2 :
		print("You have choosen to delete the element at the front")	
		new4 = DELETE_FRONT(arr, size, n)
		print(new4)
	elif delete_position == 3 :
		print("You have choosen to delete the element at the given position")
		new5 = DELETE_POSITION (arr, size, n, LOC)
		print(new5)
