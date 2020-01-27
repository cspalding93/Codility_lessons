def solution(n):
    # I can transform the binary into a string and use the split function to separate the gaps
    # binary always starts with "0b" so that part can be cut off when assigning the string/binary object
    gap_lengths = []
    binary_form = str(bin(n))[2:]
    gaps = binary_form.split("1")
    
    # the first digit in binary is always 1 so I just need to look for the ending
    # I eliminate the last item because 1.) if it ends in a 1, then it will be an empty string and ...
    # ... 2.) if it ends in a sequence of 0's, then it is not a gap
    del gaps[-1]           
    
    # since all the 0 sequences are strings, a set will reduce the items to search and now I just need the length of the string!
    # if the length of the set is 0, then there are no gaps to count, return 0
    if len(set(gaps)):
        return max(map(lambda x: len(x), gaps))
    else:
        return 0