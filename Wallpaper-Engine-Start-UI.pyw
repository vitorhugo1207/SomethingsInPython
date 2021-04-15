import PySimpleGUI as sg
import os

# Elementos e extração de dados
sg.theme('Reddit')
layout = [
    [sg.Text('Open Wallpaper Engine?')],
    [sg.Button('Yes',size=(20,1)), sg.Button('No',size=(20,1))],
]
# Window
janela = sg.Window('Open Wallpaper Engine?', layout)

# Eventos e processamento de dados
while True:
    events, values = janela.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Yes':
        os.startfile('D:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine\wallpaper32.exe')
        break
    if events == 'No':
        break
