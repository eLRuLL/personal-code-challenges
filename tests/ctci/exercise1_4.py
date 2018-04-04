"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
"""
import random


def check_palindrome_permutation(string):
    d = {}
    for x in string:
        if d.get(x):
            d[x] = 0
        else:
            d[x] = 1

    extra_index = 0
    for _, v in d.items():
        extra_index += v

    if (len(string) % 2) == 0:
        return extra_index == 0
    else:
        return extra_index == 1


def test_palindrome_permutation():
    palindromes = [
        'a',
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba',
    ]

    for palindrome in palindromes:
        shuffled = list(palindrome)
        random.shuffle(shuffled)
        assert check_palindrome_permutation(''.join(shuffled))

    palindrome_phrases = [
        'able was i ere i saw elba',
    ]

    for palindrome in palindrome_phrases:
        assert check_palindrome_permutation(palindrome)

    not_palindromes = [
        'ab',
        '12312412501924ngijsfskcmsakdasnbgp',
        'aaaaab',
    ]

    for not_palindrome in not_palindromes:
        shuffled = list(not_palindrome)
        random.shuffle(shuffled)
        assert not check_palindrome_permutation(''.join(shuffled))
