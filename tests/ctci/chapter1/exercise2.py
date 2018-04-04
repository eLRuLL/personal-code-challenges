"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""
from collections import defaultdict


def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        characters = defaultdict(int)
        for x in str1:
            characters[x] += 1
        for x in str2:
            if characters.get(x):
                characters[x] -= 1
            else:
                return False
    return True


def test_check_permutation():
    assert is_permutation('aaaab', 'abaaa')
    assert is_permutation('bbbaaaabbbcccqwertyuiop', 'qwertyuiopbbbaaaabbbccc')
    assert not is_permutation('bbbbbb', 'aaaaaa')
