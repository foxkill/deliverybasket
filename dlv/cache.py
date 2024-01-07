#
# dlv:cache
#

import os
from typing import Final
from .basket import Basket
from .future import Future

CACHE_DIRECTORY: Final = '.bcache'

class Cache():
    def __init__(self, basket: Basket):
        self.basket = basket

    def put(self):
        if not self.create_cache_dir_if_not_exits():
            raise ValueError(f'Cant create cach directory: {self.get_cache_directory()}')

        serializedString = self.basket.serialize()
        filename = self.get_filename()

        with open(filename, 'w+') as f:
            f.write(serializedString)
        
        return True
    
    def get_filename(self) -> str:
        return self.get_cache_directory() + \
            os.sep + \
            (self.basket.get_future().long_code + '-' + self.basket.hashcode()).lower() + \
            '.yaml'

    def cache_basket(self, future: Future, basket: Basket) -> bool:
        # basket.serialize()
        if not self.create_cache_dir_if_not_exits():
            raise ValueError(f'Cant create cach directory: {self.get_cache_directory()}')

        return True

    def get_cache_directory(self) -> str:
        return os.curdir + os.sep + CACHE_DIRECTORY

    def create_cache_dir_if_not_exits(self) -> str:
        dirname = self.get_cache_directory()

        if os.path.exists(dirname):
            return dirname

        try:
            os.mkdir(dirname)
        except Exception as e:
            dirname = ''

        return dirname