def partition(lst, fn):
    """Partition lst by predicate.

     - lst: list of items
     - fn: function that returns True or False

     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0

        >>> def is_string(el):
        ...     return isinstance(el, str)

        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]

        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    # list comprehension for True in a, false in b
    a = [el for el in lst if fn(el) is True]
    b = [el for el in lst if fn(el) is False]

    # print(a)
    # print(b)

    return [a, b]

    # works but too long and not easy to read
    # return [[el for el in lst if fn(el) is True], [el for el in lst if fn(el) is False]]
