# ABOUT

# QUICK SORT

    Write a program to sort the elements of array using Quick Sort.

## PSEUDO CODE

    QUICKSORT(A,START,END):
        IF START < END:
            PIVOT_INDEX = PARTITION(A,START,END)
            QUICKSORT(A,START,PIVOT_INDEX - 1)
            QUICKSORT(A,PIVOT_INDEX + 1, END)
        END OF IF
    
    PARTITION(A,START,END):
        PIVOT = A[END]
        I = START
        FOR J = START TO END:
            IF A[J] < PIVOT:
                SWAP(A[J],A[I])
                I = I + 1
            END OF IF
        END OF FOR
        SWAP(A[I+1],PIVOT)
        RETURN I+1