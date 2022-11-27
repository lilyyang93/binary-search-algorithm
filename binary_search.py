import math 

def binary_search(val_to_find, l_to_search):
    l_to_search.sort()
    lo = 0 
    hi = len(l_to_search)-1


    while lo <= hi:
        mid = math.floor((hi+lo)/2)
        if l_to_search[mid] == val_to_find:
            return mid
        elif val_to_find > l_to_search[mid]:
            lo = mid+1 
        elif val_to_find < l_to_search[mid]:
            hi = mid-1
    return -1 

