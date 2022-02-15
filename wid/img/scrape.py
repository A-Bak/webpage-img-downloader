from typing import List

import re
import traceback

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.common.exceptions import WebDriverException

from webdriver_manager.chrome import ChromeDriverManager



def validate_url(url: str) -> bool:

    if not isinstance(url, str):
        print('TypeError: Target URL is not a string type: \'{}\'.'.format(url))
        raise TypeError    
    
    # TODO: separete regex for when HTTP protocol is not specified
    url_regex = ("((http|https)://)(www.)?" +
                "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                "{2,256}\\.[a-z]" +
                "{2,6}\\b([-a-zA-Z0-9@:%" +
                "._\\+~#?&//=]*)")
    
    url_pattern = re.compile(url_regex)
    
    if not url_pattern.match(url):
        print('ValueError: Invalid target URL: \'{}\'.'.format(url[:30]))
        raise ValueError    
    
    return True



def find_image_urls(target_url: str) -> List[str]:
    
    validate_url(target_url)
    
    # Initialize a windowless Chrome webdriver for interacting with the website
    # + hide the browser window and suppress all but fatal error/warning msgs
    chrome_driver_path = ChromeDriverManager().install()

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--log-level=3')
    
    driver = webdriver.Chrome(chrome_driver_path,
                              chrome_options=chrome_options)
    
    try:
        driver.get(target_url)
      
        image_elements = driver.find_elements_by_tag_name('img')
        image_urls = [get_element_src(e, target_url) for e in image_elements]

        driver.close()

    except WebDriverException:
        print('Error: Could not resolve site \'{}\'.'.format(target_url))
        
    except:
        traceback.print_exc()

    finally:
        driver.quit()

    return image_urls



def get_element_src(element: WebElement, base_url: str = '') -> str:
    
    # Elements with URLs
    if element.get_attribute('src'):
        return element.get_attribute('src')
        
    # Elements with just URIs -> prepend base address
    elif element.get_attribute('data-src'):
        return base_url + element.get_attribute('data-src')
    
    # Element has neither attribute -> missing a link?
    else:
        return None
    
    

def get_page_source(url: str) -> str:
    
    validate_url(url)       