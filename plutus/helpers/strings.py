"""
File: strings.py
Project: plutus
File Created: Thursday, 29th June 2023 08:27:46 am
"""
import re

class BinaryFileAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def findstrings(self):
        with open(self.filename, "rb") as f_binary:
            return re.findall("([a-zA-Z]{4,})", str(f_binary.read())) # find all strings with 4 or more characters
