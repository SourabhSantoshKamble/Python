# ABOUT

# BINARAY SEARCH

    Write a program to search an element in an array using Binary Search

## PSEUDO CODE

    BINARY SEARCH(A,KEY,N):
        BEG = 0
        END = N - 1
        WHILE BEG <= END:
            MID = (BEG + END)/2
            FOR I = 0 TO N :
                IF KEY == A[MID]:
                    RETURN MID
                END OF IF
                ELSE IF KEY < A[MID]:
                    END = MID - 1
                END OF ELSE IF
                ELSE:
                    BEG = MID + 1
                END OF ELSE
            END OF FOR
        END OF WHILE
        RETURN -1