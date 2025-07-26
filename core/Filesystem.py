from os import PathLike
from pathlib import Path

from core import (
    TextAnsiFormatter,
    int_input
)

CLOSE_MENU_CODE: int = 666


class FileSystem:
    """
    Simple wrapper class for interaction with file system
    """

    current_dir: str | PathLike

    def __init__(self, current_directory: str):
        self.current_dir = current_directory

    def move_upper(self):
        """
        Move upper in file system tree
        :return: None
        """

        self.current_dir = Path(self.current_dir).parent

    def move_lower(self):
        """
        Move lower in file system tree
        :return: None
        """
        p = Path('.')  # check current directory
        dir_list = [x for x in p.iterdir() if x.is_dir()]
        TextAnsiFormatter.prGreen('Available directories:')
        if len(dir_list) == 0:
            TextAnsiFormatter.prRed('There are no directories nearby')
        else:
            dir_counter = 0  # change value to zero if you are programmer
            for dir in dir_list:
                print(f'{dir_counter}: {dir.name}')
                dir_counter += 1

            print()  # just empty line
            print(f'Or {CLOSE_MENU_CODE}: to exit this menu')

            while True:
                dir_number = int_input('Enter dir number to move in')
                if dir_number in range(len(dir_list)):
                    self.current_dir = dir_list[dir_number].as_posix()
                    break
                elif dir_number == int(CLOSE_MENU_CODE):
                    TextAnsiFormatter.prYellow('Close menu')
                    break
