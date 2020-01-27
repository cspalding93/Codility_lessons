def solution(A):
    res = 0
    for e in A:
        res = res^e
    return res