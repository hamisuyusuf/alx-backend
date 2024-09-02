#!/usr/bin/env python3
""" 0-simple_helper_function """


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
