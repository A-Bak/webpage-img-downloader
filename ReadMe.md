# Webpage Image Downloader
---
Webpage image downloader (wid) is a python package for finding and saving images from webpages. It uses Selenium's Chrome webdriver to scrape image elements from web pages and extracting their source URLs. The images are downloaded using Python `urllib.request` or `requests` packages.



## Instalation
---
You can use pip to install the package wid.
```
pip install wid
```

## Executables
---
The `wid` package includes two executables `wid-downloader` and `wid-crawler`.

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

## Webcrawler Instructions
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
            image_elements = webdriver.find_elements_by_class_name('wp-manga-chapter-img')
            return image_elements
        
        except NoSuchElementException:
            return []
    
__InstructionClass__ = WebCrawlerInstructions
```

## Examples
---

