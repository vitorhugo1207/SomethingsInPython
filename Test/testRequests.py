import requests
import json

re = requests.get("http://www.fateclins.edu.br/v4.0/vagasEstagioEmprego.php")

html = re.text

htmlFind = html.find('Emprego')


print(re.headers['content-type'])