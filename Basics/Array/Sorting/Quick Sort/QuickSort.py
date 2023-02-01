# Quick Sort Demonstration


# Partition function definition
def Partition(arr,beg,end):
    # pivot variable definition
    pivot = arr[end]
    i = beg - 1
    for j in range(beg,end):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1

# QuickSort function definition
def QuickSort(arr,beg,end):
    if beg < end:
        pivot_index = Partition(arr,beg,end)
        QuickSort(arr,beg,pivot_index - 1)
        QuickSort(arr,pivot_index+1,end)

# list creation
arr = [50,23,9,18,61,32]
print("\nArray elements before swap : [",end = " ")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("]\n")
end = len(arr) - 1
# Quicksort function call
QuickSort(arr,0,end)
print("\nArray elements after swap : [",end = " ")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("]\n")