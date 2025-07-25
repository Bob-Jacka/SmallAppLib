"""
File with library positive tests
"""
from core.TextAnsiFormater import TextAnsiFormatter
from core.UserOutput import (
    column_output_with_counter2,
    column_output_with_headers
)

if __name__ == '__main__':
    print('Underline style: ', end='')
    TextAnsiFormatter.prUnderline('Hello world')
    print('Bound style: ', end='')
    TextAnsiFormatter.prBoundText('Hello world')
    print('Italic style: ', end='')
    TextAnsiFormatter.prItalic('Hello world')

    print('Print in color - white: ', end='')
    TextAnsiFormatter.prWhite('Hello world')

    print('Print in color - blue: ', end='')
    TextAnsiFormatter.prBlue('Hello world')

    print('Print in color - red: ', end='')
    TextAnsiFormatter.prRed('Hello world')

    print('Print in color - black: ', end='')
    TextAnsiFormatter.prBlack('Hello world')

    print('Print in color - green: ', end='')
    TextAnsiFormatter.prGreen('Hello world')

    print('Print in color - yellow: ', end='')
    TextAnsiFormatter.prYellow('Hello world')

    print('Print in color - cyan: ', end='')
    TextAnsiFormatter.prCyan('Hello world')

    print('Print in color - light gray: ', end='')
    TextAnsiFormatter.prLightGray('Hello world')

    print('Print in color - purple: ', end='')
    TextAnsiFormatter.prPurple('Hello world')

    print('Print in color - aquamarine: ', end='')
    TextAnsiFormatter.prAquamarine('Hello world')

    print('Constructor output function: ')
    TextAnsiFormatter.construct_string('Hello world', 'no-underline', 'no-bound', 'no-fill_bg')  # simple Hello world
    TextAnsiFormatter.construct_string('Hello world')  # simple Hello world, without giving other arguments

    TextAnsiFormatter.construct_string('Hello world', 'underline', 'no-bound', 'no-fill_bg')  # simple Hello world with underline
    TextAnsiFormatter.construct_string('Hello world', 'no-underline', 'bound', 'no-fill_bg')  # simple Hello world with bound
    TextAnsiFormatter.construct_string('Hello world', 'no-underline', 'no-bound', 'fill_bg')  # simple Hello world with fill background
    TextAnsiFormatter.construct_string('Hello world', 'no-underline', 'no-bound', 'no-fill_bg', 'crossed')  # simple Hello world with crossed

    list_to_iterate = ['1', '2', '3', '4', '5', '6']
    headers = ['firstH', 'secH', 'thirdH']

    print()
    column_output_with_counter2(list_to_iterate)
    print()
    column_output_with_headers(list_to_iterate, headers, 3)
