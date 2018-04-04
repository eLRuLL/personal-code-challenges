"""
URLify: Write a method to replace all spaces in a string with '%20': You may assume that the string has sufficient space
at the end to hold the additional characters, and that you are given the "true" length of the string.
(Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
"""


def urlify(string):
    new_string = []
    for x in string:
        if x == ' ':
            new_string.append('%20')
        else:
            new_string.append(x)

    return ''.join(new_string)


def test_urlify():
    assert urlify('   ') == '%20%20%20'
    assert urlify('Mr John Smith') == 'Mr%20John%20Smith'
