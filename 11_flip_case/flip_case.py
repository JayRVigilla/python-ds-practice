def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    ans = ''

    for char in phrase:
        if char.lower() == to_swap:
            if char == to_swap:
                ans += char.upper()
            else:
                ans += char.lower()
        else:
            ans += char
        #     change = to_swap.upper()
        # if to_swap.lower() == to_swap:
        #     change = to_swap.upper()
        # else:
        #     change = to_swap.lower()
    return ans
