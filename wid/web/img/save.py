from typing import List

import os

from urllib.request import urlretrieve

from web.url import Url

import file.utils




             
def save_images(url_list: List[Url], path_to_dir: str) -> None:
    """
    Save a set of images from a list of URLs to a location on disk.
    
    Requires a list of URLs url_list and a location path_to_dir.
    Each individual image is saved using web.img.save.download_image()
    function. If there are any missing directories on the path_to_dir,
    they are created using file.utils.create_dir().
    
    """    
    file.utils.create_dir(path_to_dir)
    
    for url in url_list:
        
        try:
            print('Downloading image from \'{}\'.'.format(url))
            download_image(url, path_to_dir)
        
        except:
            print('Could not retrieve image from \'{}\'.'.format(url))



def download_image(url: Url, path_to_dir: str = './') -> None:
    """
    Download a single image pointed to by a URL and save it to a
    location on the disk.
    
    Requires a URL argument. If a location is not provided by a
    path_to_dir argument, then the default './' working directory
    is used to store the image.
    
    Name of the image file is the basename of the path portion of the URL.
    It is the string after last '/' symbol e.g.:
    https://duckduckgo.com/assets/icons/header/reddit.svg -> reddit.svg
        
    """
    if url is not None:
        img_path = url.path
        img_basename = os.path.basename(img_path)
        save_file_path = os.path.join(path_to_dir, img_basename) 
        
        urlretrieve(url, save_file_path)
        

            