def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    # have location give index for beginning or end
    locIndex = None

    if location != "beginning":
        if location != "end":
            return None
    if location == "beginning":
        locIndex = 0
    else:
        locIndex = -1

    # # handles invalid command
    # if command != "remove":
    #     if command != "add":
    #         return None

    # create remove situation
    if command == "remove":
        return lst.pop(locIndex)

    # create add situation
    if command == "add":
        if locIndex == 0:
            lst.insert(locIndex, value)
        else:
            # insert didn't always add to end of lst,
            # sometimes to second to last. Why?
            lst.append(value)
        return lst
    # handles invalid command
    else:
        return None
