# Program to sort elements of Array using Insertion Sort

# import libraries
import array as ar

# Insertion Sort function definition
def InsertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print("The sorted array is : [",end=" ")
    for i in range(len(arr)):
        print(arr[i],end="  ")
    print(" ]\n ")
# array initialization
arr = ar.array('i',[25,33,5,69,25,55,102,30])
# Displaying original array elements
print("\nArray before Sorting : [",end=" ")
for i in range(len(arr)):
    print(arr[i],end="  ")
print(" ] \n")
# Insertion Sort function call
InsertionSort(arr)