def check_permutation(s1, s2):
    """Given 2 strings, decide if one is a permutation of the other"""

    # quick fail for strings of differing lengths
    if len(s1) != len(s2):
        return False

    letters = {}
    for letter1 in s1:
        letters[letter1] = letters.get(letter1,0)+1

    for letter2 in s2:
        if letters.get(letter2,0) == 0:
            return False

        else:
            letters[letter2] -= 1

    return True

if __name__ == '__main__':
    
    assert check_permutation('abcd', 'help') == False
    assert check_permutation('goodbye', 'dbyeogo') == True
    print("Tests passed")