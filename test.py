import requests

url = "https://zajecia-programowania-xd.pl/flagi"
raw_input = requests.get(url)
text = raw_input.text
lista_linii = text.split('</p>')
for linia in lista_linii:
    if '.pl' or '.com' in linia:
        print(linia)

            