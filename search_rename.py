from os import rename, listdir, walk, path
from fnmatch import fnmatch
import logging

logging.basicConfig(filename='phone_rename.log',
                    encoding='utf-8', level=logging.DEBUG)

folder = '/data/ftp/FTP/CPE/'

# folder = '/data/ftp/FTP/CPE/10053066/'

for dirname, dirs, files in walk(folder):
    for file in files:
        if fnmatch(file, '*-phone.cfg'):
            #rename(path.join(dirname,file), path.join(dirname,file).lower())
            rename(dirname + "/" + file, dirname + "/" + file.lower())
            #print(dirname + "/" + file)
