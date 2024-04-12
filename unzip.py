import sys
import os
import zipfile
from zipfile import ZipFile

def __unzip(source_dir, target_dir):

    folders_to_extract = [ f.path for f in os.scandir(source_dir) if zipfile.is_zipfile(f) ]

    for file_name in folders_to_extract:
        if zipfile.is_zipfile(file_name):
            with ZipFile(file_name, 'r') as zip: 
                print('Extracting ', file_name) 
                zip.extractall(path = target_dir)
                zip.close()
                print('Done!')
            
if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        source_dir = os.getcwd()
    
    if len(sys.argv) > 2:
        target_dir = source_dir + '\\' + sys.argv[2]
    else:
        target_dir = None    
    
    __unzip(source_dir, target_dir)