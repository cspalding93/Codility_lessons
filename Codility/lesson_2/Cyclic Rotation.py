def solution(A):
    # filter empty arrays/lists
    if len(A):
        while K > len(A):
            K -= len(A)
        return A[-K::] + A[:-K:]
    else:
        return A