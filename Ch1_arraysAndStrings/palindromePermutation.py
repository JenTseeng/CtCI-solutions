def is_palindrome_permutation(s):
    """ Function to check if string is a permutation of a palindrome"""

    # assuming case insensitive, standardizing format
    s = s.lower()

    # create hashmap with all letters
    letters = {}
    for letter in s:
        letters[letter] = letters.get(letter,0) + 1

    num_odd = 0
    for value in letters.values():
        if value%2 != 0:            
            num_odd += 1

            if num_odd > 1:
                return False

    return True

if __name__ == '__main__':

    assert is_palindrome_permutation('hello') == False
    assert is_palindrome_permutation('RACEcar') == True
    assert is_palindrome_permutation(' ') == True
    print('tests passed')