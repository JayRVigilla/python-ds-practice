def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    # counter for occurence
    count = 0
    # iterate over word
    # if char.lower() == letter.lower()then increment count
    for char in word:
        if char.lower() == letter.lower():
            count += 1
    return count

# could've been
# return word.lower().count(letter.lower())