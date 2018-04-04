"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def unique_characters(string):
    a = {}
    for c in string:
        if c in a:
            return False
        a[c] = True


def test_unique_characters():
    repeated_chars = 'aaaaaaaaaa'
    unique_chars = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./'

    assert not unique_characters(repeated_chars)
    assert unique_chars
