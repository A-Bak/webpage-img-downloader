import click
import pyperclip

import img.save
import img.scrape




@click.command()
@click.option('--url', '-u', default=None, help='Url of the website containing desired images.')
@click.option('--target_dir', '-t', default='./wid_images', help='Target directory used to store images.')
@click.option('--img_regex', '-r', help='Regex for finding specific subset of images on the website.')

@click.option('--img-info', '-i', is_flag=True, help='Option to only find and print all image URLs on the website.')
def execute(url, target_dir, img_regex, img_info):
    
    """ Python script for extracting and saving images from websites. """
        
    target_url = pyperclip.paste() if url is None else url
        
    # Find URLs for all images on target website   
    try:
        click.echo("Starting to parse {}...".format(url))
        
        image_urls = img.scrape.find_image_urls(target_url)
        
    except ValueError:
        
        print('ValueError: Invalid target url: {}.'.format(target_url[:30]))
    
    # Filter images
    
    
    
    if img_info:
        # Print the URLs of images 
        print("Images found:")
        for url in image_urls:
            print(url)
            
    else:
        # Store images in target location
        img.save.save_images(image_urls, target_dir)    

    click.echo("Done.")





if __name__ == "__main__":
    
    execute()