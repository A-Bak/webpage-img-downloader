from typing import List

import os

from urllib.parse import urlparse
from urllib.request import urlretrieve

import file.utils

from web.url import Url



            
            
            
def save_images(url_list: List[Url], path_to_dir: str) -> None:
    
    file.utils.create_dir(path_to_dir)
    
    for url in url_list:
        
        try:
            print('Downloading image from \'{}\'.'.format(url))
            download_image(url, path_to_dir)
        
        except:
            print('Could not retrieve image from \'{}\'.'.format(url))



def download_image(url: Url, path_to_dir: str = './') -> None:
    
    if url is not None:
        
        # Name of the image is the string after last '/' symbol
        # E.g.: https://duckduckgo.com/assets/icons/header/reddit.svg -> reddit.svg
        
        img_path = url.path
        img_basename = os.path.basename(img_path)
        save_file_path = os.path.join(path_to_dir, img_basename) 
        
        urlretrieve(url, save_file_path)
        

            