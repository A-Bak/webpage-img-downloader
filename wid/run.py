import click

import imgscrape




@click.command()
@click.option('--url', default='https://duckduckgo.com/', help='Url of the website containing desired images.')
@click.option('--target', default='./wid_images', help='Target directory used to store images.')
@click.option('--img_regex', help='Regex for finding specific subset of images on the website.')
def execute(url, target, img_regex):
    
    """ Python script for extracting and saving images from websites. """
    
    click.echo("Starting to parse {}...".format(url))
    
    imgs = imgscrape.extract_images(url)
    
    # Store images somewhere        
    
    click.echo("Done.")
        
    return None




if __name__ == "__main__":
    
    execute()