from ctypes.wintypes import tagRECT
import click

import imgscrape
import pyperclip




@click.command()
@click.option('--url', default=None, help='Url of the website containing desired images.')
@click.option('--target', default='./wid_images', help='Target directory used to store images.')
@click.option('--img_regex', help='Regex for finding specific subset of images on the website.')
def execute(url, target, img_regex):
    
    """ Python script for extracting and saving images from websites. """
    
    click.echo("Starting to parse {}...".format(url))
    
    if url is None:
        target_url = pyperclip.paste()
    else:
        target_url = url
        
    try:
        
        imgscrape.extract_images(target_url)
        
    except ValueError:
        
        print('ValueError: Invalid target url: {}.'.format(target_url[:30]))
    
    
    # Store images somewhere        
    
    click.echo("Done.")
        
    return None




if __name__ == "__main__":
    
    execute()