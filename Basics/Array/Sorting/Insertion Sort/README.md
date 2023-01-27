# ABOUT

# INSERTION SORT

    Sort the elements of an array using insertion sort.

## Pseudo code :

    InsertionSort(A):
        for i = 1 to N
            key = A[i]
            j = i - 1
            while j >= 0 and A[j] > key
                A[j+1] = A[j]
                j = j - 1
            End of while
            A[j+1] = key
        End of for
