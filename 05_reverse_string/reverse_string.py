def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    ans = ''
    for index in range(len(phrase)-1, -1, -1):
        ans += phrase[index]
    return ans
