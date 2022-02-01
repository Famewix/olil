from dotenv import load_dotenv
import os
import sys
import subprocess
from _parser import Parser
from tabulate import tabulate
from colorama import Fore, init
init(autoreset=True)

load_dotenv()

BASE_DIR = os.getenv('BASE_DIR')
parser = Parser()

def check_mpv():
    from shutil import which

    if which('mpv') == None:
        print(f'{Fore.RED}mpv not found.')
        sys.exit()


def generate_table():
    table = []
    table.append(['ID', 'Title', 'Actors', 'Tags', 'Studio'])
    for index, file in enumerate(os.listdir(BASE_DIR)):
        row = parser.parse_filename(file)
        row.insert(0, index)
        table.append(row)
    return table

def display_table(tbl):
    print(tabulate(tbl, headers='firstrow', tablefmt='fancy_grid'))

def get_id_input(lst):
    while True:
        try:
            v_id = int(input(f"{Fore.CYAN}video ID: "))
            if v_id > len(lst)-1 or v_id < 0:
                print(f"{Fore.RED}too big || too small")
            else:
                return v_id
        except ValueError:
            print(f"{Fore.RED}a positive integer is defined as a number that produces 0 when it is added to the corresponding positive integer.")

def user_choice():
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}

    choice = input(f"{Fore.CYAN}want to watch other videos? (Y/n): ").lower()
    if choice in yes:
        pass
    elif choice in no:
        sys.exit()

def main():
    check_mpv()
    while True:
        table = generate_table()
        display_table(table)
        file_paths = [os.path.join(BASE_DIR, abs_file) for abs_file in os.listdir(BASE_DIR)]
        input_id = get_id_input(file_paths)
        file_to_play = file_paths[input_id]

        if bool(os.getenv('FULLSCREEN')):
            subprocess.call(['mpv', '-fs', str(file_to_play)])
            print('studio')
        else:
            subprocess.call(['mpv', str(file_to_play)])
            print('aa')


        os.system('cls' if os.name == 'nt' else 'clear')
        user_choice()

if __name__ == "__main__":
    main()