import os
import re
import traceback

from urllib.parse import urlparse
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.common.exceptions import WebDriverException

from webdriver_manager.chrome import ChromeDriverManager



def validate_url(url: str) -> bool:

    if not isinstance(url, str):
        raise TypeError    
    
    # TODO: separete regex for when HTTP protocol is not specified
    url_regex = ("((http|https)://)(www.)?" +
                "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                "{2,256}\\.[a-z]" +
                "{2,6}\\b([-a-zA-Z0-9@:%" +
                "._\\+~#?&//=]*)")
    
    url_pattern = re.compile(url_regex)
    
    if not url_pattern.match(url):
        raise ValueError    
    
    return True



def extract_images(target_url: str) -> None:
    
    validate_url(target_url)
    
    # Initialize a windowless Chrome webdriver for interacting with the website
    chrome_driver_path = ChromeDriverManager().install()

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--log-level=3')
    
    driver = webdriver.Chrome(chrome_driver_path,
                              chrome_options=chrome_options)
    
    try:
        driver.get(target_url)
      
        image_list = driver.find_elements_by_tag_name('img')
        
        for img_element in image_list:
                
                img_src = get_element_src(img_element, target_url)
                download_image(img_src)

        driver.close()

    except WebDriverException:
        print('Error: Could not resolve site \'{}\'.'.format(target_url))
        
    except:
        traceback.print_exc()

    finally:
        driver.quit()



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
    
    

def download_image(url: str, target_dir: str = 'out/') -> None:
    
    if url is not None:
        
        # Name of the image is the string after last '/' symbol
        # E.g.: https://duckduckgo.com/assets/icons/header/reddit.svg -> reddit.svg
        
        img_path = urlparse(url).path
        img_basename = os.path.basename(img_path)
        save_file_path = os.path.join(target_dir, img_basename) 
        
        try:
            print('Downloading image from \'{}\'.'.format(url))
            urlretrieve(url, save_file_path)
            
        except:
            print('Could not retrieve image \'{}\' from \'{}\'.'.format(img_basename, url))
                