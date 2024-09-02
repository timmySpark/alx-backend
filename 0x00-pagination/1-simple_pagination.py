#!/usr/bin/env python3
'''Task 1. Simple pagination'''
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' Return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters.
    '''
    last = page * page_size
    return last - page_size, last


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data."""
        assert page > 0 and page_size > 0
        assert isinstance(page, int) and isinstance(page_size, int)

        start, end = index_range(page, page_size)
        try:
            db = self.dataset()
            return db[start:end]
        except IndexError:
            return []
