import PySimpleGUI as sg
import subprocess as sp
import os

class UI:
    def __init__(self): 
        # Layout
        layout = [
            [sg.Text('Open'), sg.Input(key='son')],
            [sg.Button('OK')]
        ]
        # Window
        janela = sg.Window("Open Wallpaper Engine?").layout(layout)
        # Data
        self.Button, self.values = janela.Read()
    
    def Iniciar(self):
        son = self.values['son']

        if son == 's':
            os.startfile('C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine\launcher.exe')
        if son == 'y':
            os.startfile('C:\Program Files (x86)\Steam\steamapps\common\wallpaper_engine\launcher.exe')
        else:
            pass

tela = UI()
tela.Iniciar()