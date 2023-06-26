'''
File: files.py
Project: plutus
File Created: Sunday, 15th November 2020 11:46:46 am
license: 

'''
from mimetypes import MimeTypes
import os
from datetime import datetime #for converting unix timestamp to datetime

mime = MimeTypes()


'''

This function returns the file details of a file and returns a dictionary of the file details with formatted date and time

'''
def getfiledetails(path):

    infile = path
    mime_type = mime.guess_type(infile)

    filemime =  mime_type[0]
    size = os.path.getsize(infile)
    lastmodified =  datetime.fromtimestamp(os.path.getmtime(infile)).strftime('%Y-%m-%d %H:%M:%S')
    creationdate = datetime.fromtimestamp(os.path.getctime(infile)).strftime('%Y-%m-%d %H:%M:%S')
    
    return {'flename': infile, 'mime_type': filemime, 'size': size, 'lastmodified': lastmodified, 'creationdate': creationdate}

    '''
    all_details = os.stat(infile)

    print(all_details)

    #we get someting like this:
    #os.stat_result(st_mode=33252, st_ino=34409711, st_dev=16777224, st_nlink=1, st_uid=501, st_gid=20, st_size=189, st_atime=1605428774, st_mtime=1605428773, st_ctime=1605428773)
    '''
    
#print(getfiledetails('C:\\Users\\emsec\\Documents\\GitHub\\AThackathons\\README.md')) 
'''
upon calling the function we should get something like this:

{'flename': 'process.py', 'mime_type': 'text/x-python', 'size': 2401, 'lastmodified': '2023-06-26 07:35:11', 'creationdate': '2023-06-26 07:35:11'}
'''


def iterate_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            # Process the file_path as needed
            print(getfiledetails(file_path))

iterate_directory('path/to/directory')