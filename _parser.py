# Abigail Part 2 - [Lena Paul, Abigail Mac] - (Threesome) - @Tushy
import re

class Parser:
    def __init__(self) -> None:
        pass

    def get_title(self, fname):
        return fname.split('-')[0]

    def get_actors(self, fname):
        try:
            return re.search(r'\[(.*?)\]',fname).group(1)
        except AttributeError:
            return ''

    def get_tags(self, fname):
        try:
            return re.search(r'\((.*?)\)',fname).group(1)
        except AttributeError:
            return ''
    
    def get_studio(self, fname):
        return fname.split('@')[1]

    def parse_filename(self, f_name, mode="row"):
        title = self.get_title(f_name)
        actors = self.get_actors(f_name)
        tags = self.get_tags(f_name)
        studio = self.get_studio(f_name)
        if mode=="row":
            return [title, actors, tags, studio]
        else:
            return title, actors, tags, studio

        # print(title)
        # print(actors)
        # print(tags)
        # print(studio)
        # print()