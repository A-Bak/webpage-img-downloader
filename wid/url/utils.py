from typing import List

import re
import urllib




def validate_url(url: str) -> bool:

    if not isinstance(url, str):
        print('TypeError: Target URL is not a string type: \'{}\'.'.format(url))
        raise TypeError    
    
    url_regex = ("((http|https|ftp)://)(www.)?" +
                "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                "{2,256}\\.[a-z]" +
                "{2,6}\\b([-a-zA-Z0-9@:%" +
                "._\\+~#?&//=]*)")
    
    url_pattern = re.compile(url_regex)
    
    if not url_pattern.match(url):
        print('ValueError: Invalid target URL: \'{}\'.'.format(url[:30]))
        raise ValueError    
    
    return True



def has_scheme(url: str) -> bool:
    
    if not isinstance(url, str):
        raise TypeError
    
    scheme_regex = '(http|https)://.*'
    scheme_patter = re.compile(scheme_regex)
    
    if scheme_patter.match(url):
        return True
    
    else:
        return False



def set_url_scheme(url: str) -> str:
    
    parsed_url = urllib.parse.urlparse(url)
    
    if not has_scheme(url):
        scheme = "https"
        parsed_url = parsed_url._replace(scheme=scheme)
                    
        return urllib.parse.urlunparse(parsed_url)
    
    else:
        return url
    
    
def get_url_netloc(url: str) -> str:
    
    parsed_url = urllib.parse.urlparse(url)
    
    if parsed_url.netloc == '':
        raise ValueError
    
    else:
        return parsed_url.netloc
    
    

def filter_urls(url_list: List[str], regex: str) -> List[str]:
    
    pattern = re.compile(regex)
    
    filter_func = lambda x: pattern.match(x)    
    
    return list(filter(filter_func, url_list))