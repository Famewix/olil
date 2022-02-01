from dotenv import load_dotenv
import os
import subprocess
from parser import Parser
from tabulate import tabulate

load_dotenv()

BASE_DIR = os.getenv('BASE_DIR')
parser = Parser()

def generate_table():
    table = []
    table.append(['ID', 'Title', 'Actors', 'Tags', 'Studio'])
    for index, file in enumerate(os.listdir(BASE_DIR)):
        row = parser.parse_filename(file)
        row.insert(0, index)
        table.append(row)
    return table

table = generate_table()
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
input_id = int(input('ID: '))
file_paths = [os.path.join(BASE_DIR, abs_file) for abs_file in os.listdir(BASE_DIR)]
file_to_play = file_paths[input_id]

subprocess.call(['mpv', str(file_to_play)])
print('*'*14)

