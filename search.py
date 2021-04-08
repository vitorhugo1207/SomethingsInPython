import os

link = input("Search\n->").replace(' ', '+')
link2 = (f'https://www.ecosia.org/search?q={link}')
os.startfile(link2)