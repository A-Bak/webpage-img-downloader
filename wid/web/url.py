from __future__ import annotations
from typing import List

import re

import urllib




class Url(str):
    

    def __init__(self, url: str, default_scheme: str='https://') -> None:
            
            
            if not '//' in url:
                url_string = default_scheme + url
            
            else:
                url_string = url
            
            parsed_url = urllib.parse.urlparse(url_string)
            
            self.scheme = parsed_url.scheme
            self.netloc = parsed_url.netloc
            self.path = parsed_url.path
            self.params = parsed_url.params
            self.query = parsed_url.query
            self.fragment = parsed_url.fragment
            
    
    def is_valid(self) -> bool:  
        
        url_regex = ("((http|https|ftp)://)(www.)?" +
                    "[a-zA-Z0-9@:%._\\+~#?&//=]" +
                    "{2,256}\\.[a-z]" +
                    "{2,6}\\b([-a-zA-Z0-9@:%" +
                    "._\\+~#?&//=]*)")
        
        url_pattern = re.compile(url_regex)
        
        if not url_pattern.match(self.__str__()):
            return False  
        
        else:
            return True
        
        
    def has_scheme(self) -> bool:
        
        if self.scheme is not None and self.scheme != '': 
            return True
        
        else:
            return False

    
    def set_url_scheme(self, scheme: str) -> None:
    
        self.scheme = scheme
        self.url_string = self.__str__()
        
        
    def get_base_url(self) -> str:
        
        if self.scheme is not None and self.scheme != '':
            return self.scheme + '://' + self.netloc
        
        else:
            return self.netloc
    
    
    def match(self, pattern: re.Pattern) -> bool:
        
        if pattern.match(self.url_string):
            return True
        
        else:
            return False
        
        
    def __repr__(self) -> str:
        return self.__str__()
    
            
    def __str__(self) -> str:
        
        return urllib.parse.urlunparse((self.scheme,
                                        self.netloc,
                                        self.path,
                                        self.params,
                                        self.query,
                                        self.fragment))
            
    
    @staticmethod
    def filter_url_list(url_list: List[Url], regex: str) -> List[Url]:
        
        pattern = re.compile(regex)
        filter_func = lambda x: x.match(pattern)
        return list(filter(filter_func, url_list))
 

