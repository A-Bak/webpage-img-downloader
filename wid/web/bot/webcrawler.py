from typing import List, Callable

import os
from collections import deque

from selenium.common.exceptions import WebDriverException

import web.img.save
import web.img.scrape

from web.url import Url
from web.bot.instructions import Instructions


# TODO: URL normalization / canonicalization
# E.g. example.com/, example.com, example.com/index.html, example.com/index.php -> one single URL
# => Use url-normalize library for Python?


class WebCrawler():
    
    def __init__(self, instructions: Instructions, starting_url: Url, target_dir: str='./wid-images') -> None:

        if not starting_url.is_valid():
            print('ValueError: Invalid target URL: \'{}\'.'.format(starting_url))
            raise ValueError
        
        self.webdriver = None
        self.instructions = instructions
        
        self.url_queue = deque([starting_url])
        self.url_visited = set()

        self.target_dir = target_dir

                
  
    def crawl(self) -> None:
        
        self.webdriver = web.img.scrape.initialize_webdriver()
        self.instructions.validate(self.webdriver, self.url_queue[0])
        
        while len(self.url_queue) > 0:
            target_url = self.url_queue.popleft()
            print('Parsing web page \'{}\'.'.format(target_url))
            
            try:
                self._navigate_url(target_url)
                image_urls = self._find_image_urls(target_url)
                self._download_images(image_urls)

                next_urls = self._get_next_url_list(target_url)
                self.url_queue.extend(next_urls)
                   
            except WebDriverException:
                # Failed to load next web page -> continue with next in queue 
                continue
            
        self.webdriver.quit()            
            
            
            
    def _navigate_url(self, target_url: Url) -> None:
        # Add both target_url and url loaded by the webdriver in case of inconsistencies
        # -> avoid endless loop of navigation
        if self.webdriver is None:
            raise ValueError('WebDriver is not initialized in WebCrawler.')        
        
        self.webdriver.get(target_url)
        self.url_visited.add(target_url)
        self.url_visited.add(self.webdriver.current_url)
        
        
        
    def _get_next_url_list(self, current_url: Url, step_function: Callable[[Url], List[Url]]=None) -> List[Url]:
        
        if step_function is None:
            next_url_list = self.instructions.next_step(self.webdriver)
        else:
            step_function(self.webdriver)

        valid_url_list = [url for url in next_url_list if url.is_valid()]
        return [url for url in valid_url_list if url not in self.url_visited]

    
    
    def _find_image_urls(self, visited_page_url: Url) -> List[Url]:
        if self.webdriver is None:
            raise ValueError('WebDriver is not initialized in WebCrawler.')    
        
        image_elements = self.instructions.find_image_elements(self.webdriver)
        return [web.img.scrape.get_element_src(e, visited_page_url) for e in image_elements]
    
    
    
    def _download_images(self, image_urls: List[Url]) -> None:
        if self.webdriver is None:
            raise ValueError('WebDriver is not initialized in WebCrawler.') 

        url_dir_name = self.webdriver.current_url.split('/')[-2]
        dir_path = os.path.join(self.target_dir, url_dir_name)
        web.img.save.save_images(image_urls, dir_path)
        
        

    