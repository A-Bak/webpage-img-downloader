import re
import traceback

from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options as ChromeOptions

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
    
    chrome_driver_path = ChromeDriverManager().install()

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(chrome_driver_path,
                              chrome_options=chrome_options)
    
    try:
        
        driver.get(target_url)
        image_list = driver.find_elements_by_tag_name('img')
                     
        for img in image_list:
            
            img_src = get_element_src(img)
            
            if img_src is not None:
            
                img_name = img_src.rpartition('/')[-1]

                # with open('out/{}'.format(img_name), 'wb') as save_location:

                #     save_location.write(img.screenshot_as_png)
                
                try:
                    urlretrieve(img_src, 'out/{}'.format(img_name))
                except:
                    print('Could not retrieve image \'{}\'.'.format(img_name))
                    
        driver.close()

    except Exception:
        
        traceback.print_exc()

    driver.quit()
    
    return None

def get_element_src(element: WebElement) -> str:
    
    if element.get_attribute('src'):
        return element.get_attribute('src')
    
    elif element.get_attribute('data-src'):
        return element.get_attribute('data-src')
        
    else:
        return None