def binary_sort(sorted_array, length, key):
    start = 0
    end = length-1
    while start <= end:
        mid = int((start + end)/2)
        if key == sorted_list[mid]:
            print("\nEntered number %d is present at position: %d" % (key, mid))
            return -1
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("\nElement not found!")
    return -1
 
arr = []
 
size = int(input("Enter size of arr: \t"))
 
for n in range(size):
    numbers = int(input("Enter any number: \t"))
    lst.append(numbers)
 
arr.sort()
print('\n\nThe array will be sorted, the sorted array is:', arr)
 
x = int(input("\nEnter the number to search: "))
 
binary_sort(lst, size, x)