from ast import parse
import re
import urllib




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