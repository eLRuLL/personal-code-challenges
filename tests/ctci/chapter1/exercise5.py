"""
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""


def one_replace_away(source, destiny):
    edited = False
    for x, y in zip(source, destiny):
        if x != y:
            if edited:
                return False
            edited = True
    return True


def one_insert_away(source, destiny):
    i = 0
    j = 0
    destiny_len = len(destiny)
    edited = False
    while j < destiny_len:
        if source[i] == destiny[j]:
            i += 1
            j += 1
        else:
            if edited:
                return False
            edited = True
            i += 1
    return True


def one_edit_away(source, destiny):
    source_len = len(source)
    destiny_len = len(destiny)
    if source_len == destiny_len:
        return one_replace_away(source, destiny)
    elif source_len + 1 == destiny_len:
        return one_insert_away(source, destiny)
    elif source_len - 1 == destiny_len:
        return one_insert_away(source, destiny)
    else:
        return False


def test_one_away():
    test_cases = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
    ]

    for source, destiny, result in test_cases:
        assert one_edit_away(source, destiny) == result
