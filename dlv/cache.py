#
# dlv:cache
#

import os
from typing import Final, Union
from .basket import Basket
from .future import Future

CACHE_DIRECTORY: Final = '.bcache'
CACHE_FILE_EXTENSION: Final = '.yaml'

class Cache():
    def __init__(self):
        pass

    def put(self, basket: Basket):
        if not self.create_cache_dir_if_not_exits():
            raise ValueError(f'Cant create cach directory: {self.get_cache_directory()}')

        serializedString = basket.serialize()
        filename = self.get_filename(basket.future.long_code)

        with open(filename, 'w+') as f:
            f.write(serializedString)
        
        return True
    
    def get(self, filename: str) -> Union[Basket, None]:
        return Basket.from_file(filename)

    def get_filename(self, futureName: str) -> str:
        return self.get_cache_directory() + \
            os.sep + \
            futureName.lower() + \
            CACHE_FILE_EXTENSION

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