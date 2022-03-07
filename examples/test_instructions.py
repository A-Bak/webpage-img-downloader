from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from wid.web.url import Url
from wid.web.bot.instructions import Instructions




class WebCrawlerInstructions(Instructions):
    
    
    def __init__(self) -> None:
        super().__init__()
        
    
        
    def validate(self, webdriver: WebDriver, starting_url: Url) -> bool:
        pass
    
    
    
    def next_step(self, webdriver: WebDriver) -> List[Url]:
        
        try:
            xpath = "//a[@class=\"btn next_page\"]"
            element = webdriver.find_element_by_xpath(xpath)
            return [Url(element.get_attribute('href'))]
        
        except NoSuchElementException:
            return []
        
        
    
    def find_image_elements(self, webdriver: WebDriver) -> List[WebElement]:
        
        try:
            image_elements = webdriver.find_elements_by_class_name('wp-manga-chapter-img')
            return image_elements
        
        except NoSuchElementException:
            return []
        
        
    
__InstructionClass__ = WebCrawlerInstructions