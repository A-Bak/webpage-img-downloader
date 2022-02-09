import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from webdriver_manager.chrome import ChromeDriverManager


def validate_url(url):

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

def extract_images(target_url):
    
    validate_url(target_url)
    
    chrome_driver_path = ChromeDriverManager().install()

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(chrome_driver_path,
                              chrome_options=chrome_options)
    
    try:
        driver.get(target_url)
        driver.get_screenshot_as_file('capture.png')
        driver.close()
    except:
        raise ValueError
    
    return None