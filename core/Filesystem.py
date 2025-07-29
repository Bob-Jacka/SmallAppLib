import sys
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

    def resolve_cli_args(self) -> dict[str, str | int] | None:
        """
        Function for accessing CLI arguments
        :return: tuple with arguments or None if no arg given
        """
        sys_args = sys.argv
        lenght = len(sys_args)
        if lenght > 1:
            resolved_args: dict[str, str | int] = dict()  # dict with split arguments
            for param in sys_args:
                if '--' in param and '=' in param:
                    arg_pair = param.split('=')
                    arg_name = arg_pair[0]  # name of the argument, ex. web_ui_port
                    arg_value = arg_pair[1]  # value of the argument, ex. 127.0.0.1
                    resolved_args[arg_name] = arg_value
                else:
                    raise Exception('Wrong argument received, expect arg with "--" and "="')
            return resolved_args
        elif lenght == 2 and sys_args[1] == 'help':
            self.print_help()
        else:
            return None

    def print_help(self, text: str = ""):
        print(f"""
        {text}
        """)
