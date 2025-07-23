"""
File with custom user console outputs
"""


def seq_output_without_counter(list_to_iterate):
    """
    Simple line by line output without counter.
    :param list_to_iterate: list with strings to output to console.
    :return: None
    """
    for dep in list_to_iterate:
        print(f'{dep}')


def seq_output_with_counter(list_to_iterate, counter_start_value: int = 0):
    """
    Simple line by line output with counter.
    :param list_to_iterate: list with strings to output to console.
    :param counter_start_value: start value of the counter.
    :return: None
    """
    dep_counter = counter_start_value
    for dep in list_to_iterate:
        print(f'{dep_counter}: {dep}')
        dep_counter += 1


def column_output_with_counter(list_to_iterate, counter_start_value: int = 0):
    """
    Function for column output, include counter
    :param list_to_iterate:
    :param counter_start_value:
    :return: None
    """
    pass


def column_output_without_counter(list_to_iterate):
    """
    Function for column output, do not include counter
    :param list_to_iterate:
    :return: None
    """
    pass
