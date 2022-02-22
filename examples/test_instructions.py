from typing import List

from selenium.webdriver.remote.webdriver import WebDriver

from wid.web.url import Url
from wid.web.bot.instructions import Instructions




class WebCrawelerInstructions(Instructions):
    
    
    def __init__(self) -> None:
        super().__init__()
        
    
        
    def validate(self, webdriver: WebDriver, starting_url: Url) -> bool:
        raise NotImplemented
    
    
    
    def next_step(self, webdriver: WebDriver) -> List[Url]:
    
        # TODO: find next set of urls on leaded web page
        # look for element -> find URL in the element -> return 
        
        # webdriver.current_url
    
        return super().next_step(webdriver)
    