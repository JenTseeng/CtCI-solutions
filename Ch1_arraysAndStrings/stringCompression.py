def compress_string(s):
    """ function to compress strings.  For example: aabcccaaaa would become
    a2b1c3a4.  If compressed string is not shorter than original, 
    original string is returned
    """

    current_char = ''
    count = 0
    compressed = ''

    # create compressed string
    for char in s:

        # increment count for repeat character
        if char == current_char:
            count += 1

        else:
            # set current_char if not already set
            if not current_char:
                current_char = char

            # add to compressed string and update current_char for new character
            else:
                compressed = compressed + current_char + str(count)
                current_char = char

            count = 1


    # last char to compressed string
    if count:
        compressed = compressed + current_char + str(count)

    if len(compressed)<len(s):
        return compressed

    else:
        return s


if __name__ == '__main__':
    assert compress_string('aabcccaaaa') == 'a2b1c3a4'
    assert compress_string('abc') == 'abc'
    assert compress_string('') == ''
    print('All tests passed')