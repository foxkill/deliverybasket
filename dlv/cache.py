#
# dlv:cache
#

import os
from typing import Final
from .basket import Basket
from .future import Future

CACHE_DIRECTORY: Final = '.bcache'

class Cache():
    def cache_basket(self, future: Future, basket: Basket) -> bool:
        # basket.serialize()
        return True

    def create_cache_dir_if_not_exits(self) -> str:
        dirname = os.curdir + os.sep + CACHE_DIRECTORY

        if os.path.exists(dirname):
            return dirname

        try:
            os.mkdir(dirname)
        except Exception as e:
            dirname = ''

        return dirname