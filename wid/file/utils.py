from typing import List, Type
from types import ModuleType

import os
import sys
import importlib

from inspect import getmembers, isclass




def create_dir(path_to_dir: str) -> None:
    
    if not os.path.isdir(path_to_dir):
        
        try:
            os.makedirs(path_to_dir)
        
        except:
            print('Error: Failed to create target_dir \'{}\'.'.format(path_to_dir))
            
            
            
def import_module(path_to_file: str) -> ModuleType:
    
    if not os.path.exists(path_to_file):
        raise FileNotFoundError('Error: File not found at location {}.'.format(path_to_file))
    
    module_name = os.path.basename(path_to_file)
    
    try:
        spec = importlib.util.spec_from_file_location(module_name, path_to_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[module_name] = module
        return module
    
    except:
        raise ImportError('Failed to import module {} from {}.'.format(module_name, path_to_file))
    
    




def get_module_classes(module: ModuleType) -> List[Type]:
    
    return [x for x in getmembers(module) if isclass(x[1])]
    return [x for x in getmembers(module) if isclass(x)]