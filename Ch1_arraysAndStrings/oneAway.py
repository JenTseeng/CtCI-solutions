def is_one_away(s1, s2):
    """determines whether strings differ by 1 insert/remove/replace"""

    if len(s1) == len(s2):
        return check_equal_length_strings(s1, s2)

    elif abs(len(s1)-len(s2)) == 1:
        shorter, longer = determine_word_sizes(s1, s2)
        return check_for_deletion(shorter, longer)

    # return False for string lengths differing by more than 1
    else:
        return False


def check_equal_length_strings(s1, s2):
    """checking for only 1 difference for equal length strings"""
    differences = 0

    for idx in range(len(s1)):    
        if s1[idx] != s2[idx]:
            differences += 1

        if differences > 1:
            return False

    return True


def check_for_deletion(shorter, longer):
    """Check for difference of 1 character deletion"""

    chars = {}
    for char1 in shorter:
        chars[char1] = chars.get(char1,0)+1

    found_extra_char = False
    for char2 in longer:
        # letter does not exist in smaller word
        if chars.get(char2,0) == 0:
            if found_extra_char:
                return False
            
            else:
                found_extra_char = True
        
        else:
            chars[char2] -= 1

    return True


def determine_word_sizes(s1, s2):
    """determine which word is shorter/longer"""
    if len(s1) > len(s2):
        smaller = s2
        larger = s1
    else:
        smaller = s1
        larger = s2

    return smaller, larger



if __name__ == '__main__':
    assert is_one_away('pale', 'ple') == True
    assert is_one_away('pales', 'pale') == True
    assert is_one_away('pale', 'bale') == True
    assert is_one_away('pale', 'bake') == False
    assert is_one_away('session', 'sesame') == False
    print('all tests passed')