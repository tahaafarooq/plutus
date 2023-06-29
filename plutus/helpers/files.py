"""
File: files.py
Project: plutus
File Created: Sunday, 25th June 2023 11:46:46 am
    @updated : Wednesday, 28th June 2023 22:56:45 pm
"""
from mimetypes import MimeTypes
import os
import hashlib
import requests
import yaml
from datetime import datetime  # for converting unix timestamp to datetime
from strings import BinaryFileAnalyzer

mime = MimeTypes()

with open('credentials.yml', 'r') as credentials:
    config = yaml.safe_load(credentials)

VT_API_KEY = config['VT_API_KEY']
"""
    We are using the VirusTotal API to get the file details. The API key is stored in a YAML file and is loaded into the config variable.
    This is only useful when the file is was alredy uploaded to VT
    by some researchers and the file is already in the VT database and Possibly the file is Malicious.
    If the file is not in the VT database, then we will get an error saying that the file is not found in the VT database.

"""


class VirusTotalAPI:
    def __init__(self, api_key):
        """
        Initializes the VirusTotalAPI class with the provided API key and sets up the base URL.
        
        Args:
            api_key (str): The API key for accessing the VirusTotal API.
        """
        self.api_key = api_key
        self.base_url = 'https://www.virustotal.com/api/v3/files/'

    def get_file_details(self, file_id):
        url = self.base_url + file_id
        headers = {'x-apikey': self.api_key}

        response = requests.get(url, headers=headers)
        return response.json()


'''

This function returns the file details of a file and returns a dictionary of the file details with formatted date and time

'''


def getfiledetails(path):
    infile = path
    md5hash = hashlib.md5(open(infile, 'rb').read()).hexdigest()
    mime_type = mime.guess_type(infile)

    analyzer = BinaryFileAnalyzer(infile) # the file to analyze
    strs = analyzer.findstrings() # get the strings and will will need to compare the strings with the known malicious strings

    filemime = mime_type[0]
    size = os.path.getsize(infile)
    lastmodified = datetime.fromtimestamp(os.path.getmtime(infile)).strftime('%Y-%m-%d %H:%M:%S')
    creationdate = datetime.fromtimestamp(os.path.getctime(infile)).strftime('%Y-%m-%d %H:%M:%S')

    vt_api = VirusTotalAPI(VT_API_KEY)
    file_details = vt_api.get_file_details(md5hash)
    print(file_details)

    return {'flename': infile, 'mime_type': filemime, 'filehash': md5hash, 'size': size, 'lastmodified': lastmodified,
            'creationdate': creationdate}

    '''
    all_details = os.stat(infile)

    print(all_details)

    #we get someting like this:
    #os.stat_result(st_mode=33252, st_ino=34409711, st_dev=16777224, st_nlink=1, st_uid=501, st_gid=20, st_size=189, st_atime=1605428774, st_mtime=1605428773, st_ctime=1605428773)
    '''


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


dir = os.getcwd()
iterate_directory(dir)
