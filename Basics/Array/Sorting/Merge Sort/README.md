# ABOUT

# MERGE SORT

    Write a program to sort the elements of array using Merge Sort

## PSEUDO CODE

    MERGESORT(A,START,END):
        IF START < END :
            MID = (START + END) / 2
            MERGESORT(A,START,MID)
            MERGESORT(A,MID+1,END)
            MERGE(A,START,END)
        END OF IF

    MERGE(A,START,MID,END):
        TEMP[END - START + 1]   # TEMP ARRAY 
        I = START
        J = MID + 1
        K = 0
        WHILE I <= MID AND J <= END :
            IF A[I] <= A[J] :
                TEMP[K] = A[I]
                K++
                I++
            END OF IF
            ELSE :
                TEMP[K] = A[J]
                K++
                J++
            END OF ELSE
        WHILE I <= MID :
            TEMP[K] = A[I]
            K++
            I++
        END OF WHILE
        WHILE J <= END :
            TEMP[K] = A[J]
            K++
            J++
        END OF WHILE
        FOR I = START TO END :
            A[I] = TEMP[I - START]
        