import subprocess

def abre(abre):
    subprocess.Popen(abre)

texto = input('-> ')

abre(texto)