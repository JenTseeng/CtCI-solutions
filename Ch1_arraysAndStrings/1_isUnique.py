def is_unique_set(s):
    """Determine if a string has all unique characters using a set"""

    unique_letters = set(s)
    return len(unique_letters)==len(s)


def is_unique_hashmap(s):
    """Determine if a string has all unique characters using a hashmap"""

    letters = {}
    for letter in s:

        # False if letter already in hashmap
        if letters.get(letter,0) != 0:
            return False

        # add letter to hashmap if not present
        letters[letter] = 1

    return True


if __name__ == '__main__':
    
    assert is_unique_set('abcd') == True
    assert is_unique_set('goodbye') == False
    assert is_unique_set('hello') == False
    assert is_unique_set(' ') == True

    assert is_unique_hashmap('abcd') == True
    assert is_unique_hashmap('goodbye') == False
    assert is_unique_hashmap('hello') == False
    assert is_unique_hashmap(' ') == True