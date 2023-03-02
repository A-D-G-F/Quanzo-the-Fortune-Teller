from pathlib import Path
import os
import re 
import platform

home_directory = os.path.expanduser('~')
sep = re.findall(r"[\w']+", str(home_directory))
if platform.system() == 'Linux':
    name= sep[1]
else:
    name= sep[2]

def fortuneteller():
    filename= Path('./Quanzo Fortune Table.csv')
    table = {}
    with open(filename) as f:
        next(f)
        for line in f.readlines():
            line = line.strip(' ').split(',')
            order = line[0]
            fortune = line[1]
            table[order]=fortune
    order = input('Hello '+ name +', I am Quanzo the Fortune Teller.\nTo hear your fortune type in the number day you were born on \n')
    while order not in table:
        print('You tell lies, try again')
        order = input()
    while order in table:
        print('Your fortune is:',str(table[order]))
        print('Input a different number or exit?')
        order = input()
    return

fortuneteller()