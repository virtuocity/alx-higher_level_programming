#!/usr/bn/python3
""" indent text """


def text_indentation(text):
    """ a function that prints a text with 2 new lines after \
        each of these characters: ., ? and :
        Args:
            text: text to parse
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    len_text = len(text)
    for i in range(len_text):
        if text[i] == '.':
            print('.')
            print()
        elif text[i] == '?':
            print('?')
            print()
        elif text[i] == ':':
            print(':')
            print()
        else:
            if (text[i] == ' ' and (text[i - 1]
                                    in ".?:" or text[i - 1] == ' ')):
                continue
            print("{}".format(text[i]), end="")
