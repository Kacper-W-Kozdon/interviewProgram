def solution(A):
    # Find the first integer greater than 0 missing from a provided list, else (return 1 if all are negative or return max(A) + 1 if all integers between min(A) and max(A) are accounted for.

    A = list(set(A))
    A.sort()

    while A:
        if A[0] < 1:
            A.pop(0)
        else:
            break
    if bool(A):        
        
        minA = A[0]
        maxA = A[-1]
    else:
        return 1

    

    B = [i for i in range(1, maxA + 1)]
    
    for idx, elem in enumerate(A):
        if B[idx] >= 1 and not elem == B[idx]:
            if B[idx] < 1:
                return 1
            else:
                return B[idx]
    if A[-1] + 1 < 1:
        return 1
    else:
        return A[-1] + 1
    pass
