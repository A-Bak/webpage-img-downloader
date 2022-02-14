import click
import pyperclip

import img.save
import img.scrape




@click.command()
@click.option('--url', default=None, help='Url of the website containing desired images.')
@click.option('--target_dir', default='./wid_images', help='Target directory used to store images.')
@click.option('--img_regex', help='Regex for finding specific subset of images on the website.')

@click.option('--info', help='Option to only find and print all image URLs on the website.')
def execute(url, target_dir, img_regex):
    
    """ Python script for extracting and saving images from websites. """
        
    target_url = pyperclip.paste() if url is None else url
        
    # Find URLs for all images on target website   
    try:
        click.echo("Starting to parse {}...".format(url))
        
        image_urls = img.scrape.find_image_urls(target_url)
        
    except ValueError:
        
        print('ValueError: Invalid target url: {}.'.format(target_url[:30]))
    
    # Filter images
    
    
    
    # Store images in target location
    img.save.create_dir(target_dir)
    
    for u in image_urls:
        img.save.download_image(u, target_dir)   
    
    
    
    click.echo("Done.")





if __name__ == "__main__":
    
    execute()