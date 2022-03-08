import click

from wid.web.url import Url
from wid.web.bot.webcrawler import WebCrawler
from wid.web.bot.instructions import Instructions

from wid.file.utils import import_module




@click.command()
@click.option('--url', '-u', default=None, help='Url of the starting website for the web crawler.')
@click.option('--instructions', '-i', default=None, help='Implementation of Instructions abstract class used by the WebCrawler.')
@click.option('--target-dir', '-t', default=None, help='Target directory used to store images.')
def execute(url, instructions, target_dir):
    
    """ Python web crawler for extracting and saving images from websites. """    

    target_url = Url(url)
    target_dir = target_dir if target_dir is not None else './wid-images'
    
    try:
        instructions_module = import_module(instructions)
        webcrawler_instructions = instructions_module.__InstructionClass__()
        
    except:
        raise ImportError('Failed to import and instantiate user-defined Instructions class from {}.'.format(instructions))

    start_crawler(webcrawler_instructions, target_url, target_dir)



def start_crawler(instructions: Instructions, starting_url: Url, target_dir: str) -> None:
    
    if not starting_url.is_valid():
        raise ValueError('ValueError: Invalid target URL: \'{}\'.'.format(starting_url))
    
    click.echo('Starting web crawler on page {}.'.format(starting_url))
    
    webcrawler = WebCrawler(instructions, starting_url, target_dir)
    webcrawler.crawl()

    click.echo('Done.')
    
    

if __name__ == "__main__":
    
    execute()