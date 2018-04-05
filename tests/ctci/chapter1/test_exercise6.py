"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
"""


def dummy_compression(string):
    char_list = []
    count_list = []
    for x in string:
        if char_list and char_list[-1] == x:
            count_list[-1] += 1
        else:
            char_list.append(x)
            count_list.append(1)

    response = ''.join(['{}{}'.format(c, count_list[i]) for i, c in enumerate(char_list)])
    if len(response) > len(string):
        return string
    return response


def test_string_compression():
    assert dummy_compression('aabcccccaaa') == 'a2b1c5a3'
    assert dummy_compression('a') == 'a'
    assert dummy_compression('ab') == 'ab'
    assert dummy_compression('abb') == 'abb'
    assert dummy_compression('abbb') == 'a1b3'
    assert dummy_compression('aabbb') == 'a2b3'
