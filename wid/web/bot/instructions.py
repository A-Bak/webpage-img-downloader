from typing import List

import abc

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from web.url import Url



class Instructions(abc.ABC):
    
    @abc.abstractmethod
    def validate(self, webdriver: WebDriver, starting_url: Url) -> bool:
        pass
    
    @abc.abstractmethod
    def next_step(self, webdriver: WebDriver) -> List[Url]:
        pass
    
    @abc.abstractmethod
    def find_image_elements(self, webdriver: WebDriver) -> List[WebElement]:
        pass
    
    

    