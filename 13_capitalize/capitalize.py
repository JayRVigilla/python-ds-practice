def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # put in the element after doing the following check
    # for element in list
    # if boolean value of element is True
    return [el for el in lst if bool(el) is True]
    # print(new_list)
