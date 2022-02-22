from typing import List, Callable

import re
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
    

    def __init__(self, instructions: Instructions, starting_url: Url, target_dir: str='./', img_regex: str=None) -> None:

        self.webdriver = None
        self.instructions = instructions
        
        self.url_queue = deque([starting_url])
        self.url_visited = set()

        self.target_dir = target_dir
        self.img_pattern = re.compile(img_regex) if img_regex is not None else None
                
  
  
    def crawl(self) -> None:
        
        self.webdriver = web.img.scrape.initialize_webdriver()
        
        if self.instructions.validate is not None:
            self.instructions.validate(self.webdriver, self.url_queue[0])
        
        while len(self.url_queue) > 0:
            target_url = self.url_queue.popleft()
            
            print('Starting to parse web page \'{}\''.format(target_url))
            
            try:
                # Navigate to next web page, find src URLs of image elements, filter image URLs, download images
                self._navigate_url(target_url)
                # image_urls = self._find_image_elements(target_url)
                # filterd_image_urls = Url.filter_url_list(image_urls, self.img_pattern)
                # web.img.save.save_images(filterd_image_urls, self.target_dir)
                
                # Get next set of URLs from current web page
                next_urls = self._get_next_url_list(target_url)
                self.url_queue.extend(next_urls)
                   
            except WebDriverException:
                # Failed to load next web page -> continue with next in queue 
                continue
            
        print('Done.')
            
            
            
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
            next_url_list = self.instructions.next_step(self.webdriver, current_url)
        else:
            step_function(self.webdriver, current_url)

        valid_url_list = [url for url in next_url_list if url.is_valid()]
        return [url for url in valid_url_list if url not in self.url_visited]

    
    
    def _find_image_elements(self, visited_page_url: Url) -> List[Url]:
        # visited_page_url -> for extracting basename in case of relative src URLs of elements
        if self.webdriver is None:
            raise ValueError('WebDriver is not initialized in WebCrawler.')    
        
        image_elements = self.webdriver.find_elements_by_tag_name('img')
        return [web.img.scrape.get_element_src(e, visited_page_url) for e in image_elements]
    
    

    