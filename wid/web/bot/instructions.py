from typing import List

import abc

from selenium.webdriver.remote.webdriver import WebDriver
from web.url import Url



class Instructions(abc.ABC):
    
    @abc.abstractmethod
    def validate(self, webdriver: WebDriver, starting_url: Url) -> bool:
        pass
    
    @abc.abstractmethod
    def next_step(self, webdriver: WebDriver) -> List[Url]:
        pass
    
    

    