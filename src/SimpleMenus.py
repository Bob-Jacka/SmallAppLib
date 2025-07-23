"""
File with already constructed menus
"""

from src.UserInput import (
    check_int_input,
    check_string_input
)
from src.UserOutput import seq_output_without_counter


def sim_menu_int(points):
    """
    Simple menu with integer input
    :param points: container with data
    :return: None
    """
    while True:
        seq_output_without_counter(points)
        check_int_input(len(points))


def sim_menu_string(points):
    """
    Simple menu with string input
    :param points: container with data
    :return: None
    """
    while True:
        seq_output_without_counter(points)
        check_string_input(len(points))


def sim_menu():
    pass
