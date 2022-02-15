import click
import pyperclip

import img.save
import img.scrape




@click.command()
@click.option('--url', '-u', default=None, help='Url of the website containing desired images.')
@click.option('--target-dir', '-t', default='./wid_images', help='Target directory used to store images.')
@click.option('--img-regex', '-r', help='Regex for finding specific subset of images on the website.')

@click.option('--img-info', '-i', is_flag=True, help='Option to find and print all image URLs on the website.')
# TODO: Change from flag to take and argument? path_to_file for saving?
@click.option('--page-source', '-p', is_flag=True, help='Option to get the source code of target website and print it (save it).')
def execute(url: str, target_dir: str, img_regex: str, img_info: bool, page_source: bool) -> None:
    
    """ Python script for extracting and saving images from websites. """
        
    target_url = pyperclip.paste() if url is None else url
    
    click.echo('Starting to parse {}...'.format(target_url))
        
    # Find URLs for all images on target website   
    try:
        image_urls = img.scrape.find_image_urls(target_url)
        
        # Filter images
        
        
        if img_info:
            # Print the URLs of images 
            print('Images found:')
            for url in image_urls:
                print(url)
                
        else:
            # Store images in target location
            img.save.save_images(image_urls, target_dir)    
    
    except:
        click.echo('Failed.')        
    
    finally:
        click.echo('Done.')





if __name__ == "__main__":
    
    execute()