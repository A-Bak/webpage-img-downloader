from typing import List

import re
import traceback

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.common.exceptions import WebDriverException

from webdriver_manager.chrome import ChromeDriverManager

from web.url import Url




def initialize_webdriver() -> WebDriver:

    # Initialize a windowless Chrome webdriver for interacting with the website
    # + hide the browser window and suppress all but fatal error/warning msgs
    chrome_driver_path = ChromeDriverManager().install()

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--log-level=3')
    
    return webdriver.Chrome(chrome_driver_path,
                            chrome_options=chrome_options)
    
    

def find_image_urls(target_url: Url) -> List[Url]:
    
    if not target_url.is_valid():
        print('ValueError: Invalid target URL: \'{}\'.'.format(target_url))
        raise ValueError
    
    driver = initialize_webdriver()
    
    try:
        driver.get(target_url)
      
        image_elements = driver.find_elements_by_tag_name('img')
        image_urls = [get_element_src(e, target_url) for e in image_elements]

        driver.close()

    except WebDriverException as e:
        print('Error: Could not resolve site \'{}\'.'.format(target_url))
        raise e

    finally:
        driver.quit()

    return image_urls



def get_element_src(element: WebElement, url: Url) -> Url:
    
    # Elements with full URLs
    if element.get_attribute('src'):
        url_string = element.get_attribute('src')
        return Url(url_string)
        
    # Elements with just URIs -> prepend base address
    elif element.get_attribute('data-src'):
        
        url_string = url.get_base_url() + element.get_attribute('data-src')
        return Url(url_string)
    
    # Element has neither attribute -> missing a link?
    else:
        return None
    
    

def get_page_source(target_url: Url) -> str:
    
    if not target_url.is_valid():
        print('ValueError: Invalid target URL: \'{}\'.'.format(target_url))
        raise ValueError        
    
    driver = initialize_webdriver()
    
    try:
        driver.get(target_url)
        
        page_source = driver.page_source
        
        driver.close()
                
    except WebDriverException as e:
        print('Error: Could not resolve site \'{}\'.'.format(target_url))
        raise e
    
    finally:
        driver.quit()
        
    return page_source