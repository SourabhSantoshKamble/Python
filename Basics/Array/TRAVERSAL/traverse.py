# ARRAY TRAVERSAL

# importing libraries
import array as ar

print("\n Array Traversal\n")
print(" Enter the size of array:",end=" ")
size = int(input())     # user input array size
arr = ar.array('i',[0 for i in range(size)])
print("\n Enter "+str(size)+" elements of array:",end=" ")
# user input array elements
for i in range(size):
    arr[i] = int(input())
# system display array elements
print("\n Array elements are \n")
for i in range(size):
    print(" arr["+str(i)+"] : "+str(arr[i]))
print()