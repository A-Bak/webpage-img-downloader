import os




def create_dir(path_to_dir: str) -> None:
    
    if not os.path.isdir(path_to_dir):
        
        try:
            os.makedirs(path_to_dir)
        
        except:
            print('Error: Failed to create target_dir \'{}\'.'.format(path_to_dir))