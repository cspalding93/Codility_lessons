def solution_1(A):
    diffs = {}

    if len(A) > 2:
        for i, b in enumerate(A, 1):
            if i != len(A):
                pre = sum(A[:i])
                post = sum(A[i:])
                diff = pre - post
                diffs.update({i:abs(diff)})
    else:
        return asb(A[0] - A[1])
    
    
    lowest_diff = 10**20
    split_key =  0 
    for k, v in diffs.items():
        if v < lowest_diff:
            lowest_diff = v
            split_key = k
    return lowest_diff