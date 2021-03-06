# Webpage Image Downloader
---
Webpage image downloader (wid) is a python package for finding and saving images from webpages. It uses Selenium's Chrome webdriver to scrape image elements from web pages and extracting their source URLs. The images are downloaded using Python `urllib.request` or `requests` packages.



## Instalation
---
You can use pip to install the package wid.
```
pip install webpage-image-downloader
```

## Executables
---
The `webpage-image-downloader` (`wid`) package includes two executables `wid-downloader` and `wid-crawler`.

```
Usage: wid-downloader [OPTIONS]

  Python script for extracting and saving images from websites.

Options:
  -u, --url TEXT         Url of the website containing desired images.
                         Contents of the clipboard are used if none is
                         provided.
  -t, --target-dir TEXT  Target directory used to store images.
  -r, --img-regex TEXT   Regex for finding specific subset of images on the
                         website.
  -i, --img-info         Option to find and print all image URLs on the
                         website.
  -p, --page-source      Option to get the source code of target website and
                         print it (save it).
  --help                 Show this message and exit.
```

```
Usage: wid-crawler [OPTIONS]

  Python web crawler for extracting and saving images from websites.

Options:
  -u, --url TEXT           Url of the starting website for the web crawler.
                           Contents of the clipboard are used if none is
                           provided.
  -i, --instructions TEXT  Implementation of Instructions abstract class used
                           by the WebCrawler.
  -t, --target-dir TEXT    Target directory used to store images.
  --help                   Show this message and exit.
```

## Examples wid-downloader
---

Look up all the image elements on a web page using `wid-downloader`. Some of the elements might not be explicitly visible.
```
wid-downloader -u https://www.duckduckgo.com -i
```
```
Images found:
https://www.duckduckgo.com/assets/icons/header/twitter.svg
https://www.duckduckgo.com/assets/icons/header/reddit.svg
https://www.duckduckgo.com/assets/icons/header/blog.svg
https://www.duckduckgo.com/assets/icons/header/newsletter.svg
https://duckduckgo.com/assets/add-to-browser/cppm/laptop.svg
https://duckduckgo.com/assets/home/landing/icons/search.svg
https://duckduckgo.com/assets/add-to-browser/cppm/mobile.svg
https://duckduckgo.com/assets/onboarding/arrow.svg
https://www.duckduckgo.com/assets/onboarding/bathroomguy/1-monster-v2--pre-animation.svg
https://duckduckgo.com/assets/onboarding/bathroomguy/2-ghost-v2.svg
https://duckduckgo.com/assets/onboarding/bathroomguy/3-bathtub-v2--no-animation.svg
https://duckduckgo.com/assets/onboarding/bathroomguy/4-alpinist-v2.svg
Done.
```

Download a subset of desired images using `wid-downloader` by specifying a regular expression to filter through the list of found image elements. The regular expression is matched against the source URL of the elements. The images are downloaded into the target directory.
```
wid-downloader -u https://www.duckduckgo.com -t wid-images -r '.*(header).*'
```
```
Downloading image from 'https://www.duckduckgo.com/assets/icons/header/twitter.svg'.
Downloading image from 'https://www.duckduckgo.com/assets/icons/header/reddit.svg'.
Downloading image from 'https://www.duckduckgo.com/assets/icons/header/blog.svg'.
Downloading image from 'https://www.duckduckgo.com/assets/icons/header/newsletter.svg'.
Done.
```

If you want to explicitely look through the web page source code without opening up a browser you can use the `wid-downloader` to save the source code to a file.
```
wid-downloader -u https://www.duckduckgo.com -t wid-page-source -p
```


## Examples wid-crawler
---
The `wid-crawler` can be to navigate through a series of web pages, as well as find and select specific image elements on those web pages that are to be downloaded and saved locally.

### Webcrawler Instructions
---
If you want to use the `wid-crawler` to find and download images it's necessary for you to implement the abstract class `Instructions` from `wid.web.bot.instructions`. Depending on the web pages you intend to scrape, it might be needed to first implement a way for the webcrawler to bypass site's verifiaction/validation. Otherwise, it is required to provide a way to find new URLs to visit from the `starting_url` and a way to find desired image elements on visited web pages.

An example of `wid-crawler` instructions can be found in `examples/test_instructions.py`:

```python

class WebCrawlerInstructions(Instructions):
    
    
    def __init__(self) -> None:
        super().__init__()
        
    
        
    def validate(self, webdriver: WebDriver, url: Url) -> bool:
        pass
    
    
    
    def next_step(self, webdriver: WebDriver) -> List[Url]:
        
        try:
            xpath = "//a[@class=\"btn next_page\"]"
            element = webdriver.find_element_by_xpath(xpath)
            return [Url(element.get_attribute('href'))]
        
        except NoSuchElementException:
            return []
        
        
    
    def find_image_elements(self, webdriver: WebDriver) -> List[WebElement]:
        
        try:
            xpath = '//div[@class="reading-content"]/div[@class="page-break no-gaps"]/img'
            elements = webdriver.find_elements_by_xpath(xpath)
            return elements
        
        except NoSuchElementException:
            return []
        

    
__InstructionClass__ = WebCrawlerInstructions
```

### Running webcrawler
---
```
wid-crawler -u https://www.mangaread.org/manga/one-punch-man-onepunchman/chapter-218-chapter-160/ -i examples/example_instructions.py
```


```
Parsing web page 'https://www.mangaread.org/manga/one-punch-man-onepunchman/chapter-218-chapter-160/'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/2.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/3.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/4.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/5.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/6.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/7.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/8.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/9.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/10.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/11.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/12.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/13.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/14.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/15.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/16.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/17.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/18.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/19.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/20.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/21.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/22.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/23.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/24.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/25.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/26.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/27.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/7b34c97392e0e7ea750b5663abed3f7a/28.jpeg'.
Parsing web page 'https://www.mangaread.org/manga/one-punch-man-onepunchman/chapter-219-chapter-161/'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/2.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/4.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/5.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/6.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/7.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/8.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/9.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/10.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/11.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/12.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/13.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/14.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/15.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/16.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/17.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/18.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/19.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/20.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/21.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/22.jpeg'.
Downloading image from 'https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_5db92303ed13e/572aee0c077fcf50c79b8ac758b19e9a/23.jpeg'.
Done.
```
