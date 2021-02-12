import subprocess
import os

a = "@C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
# b = "https://www.youtube.com"

# Quando o "os.startfile" tenta executar o caminho ele adiciona duas barras invertidas e isso faz com que
    # de erro. Então para solucionar o problema tem que trocar a barra invertida pela a barra normal mas
        # também não está funcionando.

a = a.replace('\', '/')
os.startfile(a)