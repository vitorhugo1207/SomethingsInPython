import os

link = str(input("Search\n-> ")).strip().replace(' ', '+')
link = (f'https://www.ecosia.org/search?q={link}')

os.startfile(link)
