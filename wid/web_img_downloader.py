import os

import click
import pyperclip

import img.save
import img.scrape

from url.utils import set_url_scheme, get_url_netloc



@click.command()
@click.option('--url', '-u', default=None, help='Url of the website containing desired images.')
@click.option('--target-dir', '-t', default='./wid_images', help='Target directory used to store images.')
@click.option('--img-regex', '-r', default=None, help='Regex for finding specific subset of images on the website.')

@click.option('--img-info', '-i', is_flag=True, help='Option to find and print all image URLs on the website.')
# TODO: Change from flag to take and argument? path_to_file for saving?
@click.option('--page-source', '-p', is_flag=True, help='Option to get the source code of target website and print it (save it).')
def execute(url: str, target_dir: str, img_regex: str, img_info: bool, page_source: bool) -> None:
    
    """ Python script for extracting and saving images from websites. """
        
    target_url = pyperclip.paste() if url is None else url
    
    # Add URL scheme if it's missing in the original URL
    target_url = set_url_scheme(target_url)

    if img_info:
        get_img_info(target_url, img_regex)
        
    if page_source:
        get_page_source(target_url, target_dir)
       
    if not img_info and not page_source:
        download_images(target_url, target_dir, img_regex)
        


def get_img_info(target_url: str, target_dir: str, img_regex: str) -> None:

    click.echo('Starting to parse {}...'.format(target_url))

    try:
        # Find URLs for all images on target website   
        image_urls = img.scrape.find_image_urls(target_url)
        
        # TODO: Filter image links

        # Print the URLs of images 
        print('Images found:')
        for url in image_urls:
            print(url)
            
    except:
        click.echo('Failed.')        
    
    else:
        click.echo('Done.')
        
        
        
def get_page_source(target_url: str, target_dir: str) -> None:

    click.echo('Attempting to open {}...'.format(target_url))

    try:
        page_src = img.scrape.get_page_source(target_url)
            
        netloc = get_url_netloc(target_url)
        file_name = netloc + '.txt'
        save_file_path = os.path.join(target_dir, file_name)
            
        with open(save_file_path, 'w') as f:
            f.write(page_src)
            
    except:
        click.echo('Failed.')        
    
    else:
        click.echo('Page source code saved.')
        
        

def download_images(target_url: str, target_dir: str, img_regex: str) -> None:
    
    click.echo('Starting to parse {}...'.format(target_url))
        
    try:
        # Find URLs for all images on target website   
        image_urls = img.scrape.find_image_urls(target_url)
        
        # TODO: Filter images
        
        
        # Store images in target location
        img.save.save_images(image_urls, target_dir)    
    
    except:
        click.echo('Failed.')        
    
    else:
        click.echo('Done.')



if __name__ == "__main__":
    
    execute()