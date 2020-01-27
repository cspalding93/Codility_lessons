def solution(A):
    return list(set(range(min(A), max(A)+1)).difference(A))[0]