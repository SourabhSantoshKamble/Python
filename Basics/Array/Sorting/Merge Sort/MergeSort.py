# Merge Sort implementation

# import libraries
import array as ar

# Merge function definition
def Merge(arr,start,mid,end):
    size = end - start +1
    # empty array initialization
    temp = ar.array('i',[0 for i in range(size)])
    i = start
    j = mid + 1
    k = 0
    while i <= mid and j <= end :
        if arr[i] <= arr[j] :
            temp[k] = arr[i]
            k += 1
            i += 1
        else :
            temp[k] = arr[j]
            k += 1
            j += 1
    # add remaining elements in sub array 1
    while i <= mid :
        temp[k] = arr[i]
        k += 1
        i += 1
    # add remaining elements in sub array 2
    while j <= end :
        temp[k] = arr[j]
        k += 1
        j += 1
    # store sorted array in actual array
    for i in range(start,end+1):
        arr[i] = temp[i - start]

# Merge Sort function definition
def MergeSort(arr,start,end):
    if start < end :
        mid = int((start + end )/ 2)
        MergeSort(arr,start,mid)
        MergeSort(arr,mid+1,end)
        Merge(arr,start,mid,end)

# Array initialization
arr = ar.array('i',[32,66,5,12,54])
# Array before sorting
print("\nArray before sorting : [",end = " ")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("] \n")
# Merge Sort function call
MergeSort(arr,0,len(arr) -1)
# Array after sorting
print("\nArray after sorting : [",end = " ")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("] \n")

