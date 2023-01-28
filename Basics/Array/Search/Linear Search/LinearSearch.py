# Linear Search

def LinearSearch(arr,key):
    for i in range(len(arr)):
        if key == arr[i]:
            pos = i + 1
            return pos
    return -1

arr = [55,16,22,33,54,19]
print("\nArray elements are : [",end="")
for i in range(len(arr)):
    print(arr[i],end=" ")
print("]\n")
print("\nEnter element to search : ",end=" ")
key = int(input())
print()
result = int(LinearSearch(arr,key))
if result > -1:
    print(str(key)+"  fount at position : "+str(result)+"\n")
else:
    print(str(key)+" not present at array\n")