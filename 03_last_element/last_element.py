def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    #if len(lst) == 0 is much more idiomatic as if not lst
    if len(lst) == 0: 
        return None
    return(lst[-1])

# if lst:
#     return lst[-1]
# would be more concise