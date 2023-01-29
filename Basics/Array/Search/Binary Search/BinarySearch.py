# Binary Search

# Binary Search function definition
def BinarySearch(arr,key):
    beg = 0
    end = len(arr) - 1
    while beg <= end:
        mid = int((beg+end)/2)
        for i in range(len(arr)):
            if key == arr[mid]:
                return mid + 1
            elif key < arr[mid]:
                end = mid - 1
            else:
                beg = mid + 1
    return -1

# Array definition
arr = [12,33,45,55,65,109]
print("\nThe array elements are : [",end=" ")
for i in range(len(arr)):
    print(arr[i],end = " ")
print("]\n")
print("\nEnter the element to be searched : ",end = " ")
# User input key
key = int(input())
# Binary Search function call
result = BinarySearch(arr,key)
if result > -1:
    print("\n"+str(key)+" found at position : "+str(result)+"\n")
else:
    print("\n"+str(key)+" not found \n")