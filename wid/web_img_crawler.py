import click

from web.url import Url
from wid.web.crawler import WebCrawler




@click.command()
@click.option('--url', '-u', default=None, help='Url of the website containing desired images.')
@click.option('--target-dir', '-t', default=None, help='Target directory used to store images.')
@click.option('--img-regex', '-r', default=None, help='Regex for finding specific subset of images on the website.')
def start_crawler(url, target_dir, img_regex):
    

    # Target URL
    # (Authentication)
    # Instruction - parse URL, retrieve following URLs
    # (Image filtering - regex)
    # (Target dir)
    # Save images

    s = set()
    
    u1 = Url('https://duckduckgo.com')
    u2 = Url('https://google.com')
    u3 = Url('https://duckduckgo.com')

    def f(a):
        return []
    
    c = WebCrawler(u1, f)
    
    c.crawl()    

    
    return


if __name__ == "__main__":
    
    start_crawler()