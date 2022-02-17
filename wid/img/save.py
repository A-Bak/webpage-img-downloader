import os

from urllib.parse import urlparse
from urllib.request import urlretrieve




def save_images(url_list: str, path_to_dir: str) -> None:
    
    create_dir(path_to_dir)
    
    for url in url_list:
        
        try:
            print('Downloading image from \'{}\'.'.format(url))
            download_image(url, path_to_dir)
        
        except:
            print('Could not retrieve image from \'{}\'.'.format(url))
            
            

def create_dir(path_to_dir: str) -> None:
    
    if not os.path.isdir(path_to_dir):
        
        try:
            os.makedirs(path_to_dir)
        
        except:
            print('Error: Failed to create target_dir \'{}\'.'.format(path_to_dir))



def download_image(url: str, path_to_dir: str = './') -> None:
    
    if url is not None:
        
        # Name of the image is the string after last '/' symbol
        # E.g.: https://duckduckgo.com/assets/icons/header/reddit.svg -> reddit.svg
        
        img_path = urlparse(url).path
        img_basename = os.path.basename(img_path)
        save_file_path = os.path.join(path_to_dir, img_basename) 
        
        urlretrieve(url, save_file_path)
        

            