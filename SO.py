n = int(input("Enter the number of elements : "))
size = int(input("Enter the desired size of the array : "))
data = int(input("Enter the data to be pushed : "))
arr = [2,3,4,None,None]
arr1 = [1,3,5,None,None]
top = n-1
def push(top , arr , size, data) :
	if top == size-1 :
		print("Stack Overflow")
	else : 
		top = top+1
		arr[top] = data
	return arr
def pop(top, arr, size) :
	if top == -1 :
		print("Stack Underflow")
	else :
		arr[top] = None
		top = top-1
	return arr
print(push(top , arr , size, data))
print(pop(top, arr1, size))
	
