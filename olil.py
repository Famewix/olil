from json import load
from unicodedata import category
from dotenv import load_dotenv
import os
from parser import Parser

load_dotenv()

BASE_DIR = os.getenv('BASE_DIR')
parser = Parser()

parser.parse_filename("Abigail Part 2 - [Lena Paul, Abigail Mac] - (Threesome) - @Tushy")
