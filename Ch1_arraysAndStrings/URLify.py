def make_url(s):
    """ Replacing apaces in string with '%20' """
    chars = list(s)
    for idx, char in enumerate(chars):
        if char == ' ':
            chars[idx] = '%20'

    return ''.join(chars)


if __name__ == '__main__':
    
    assert make_url('hello world ') == 'hello%20world%20'
    assert make_url('  ') == '%20%20'
    print("Tests passed")