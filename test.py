import requests

url = "https://www.wscad.com/HELP/Polish/WSCAD64/SUITE/50AddOns/Add-On_PI-Diagram.htm"
raw_input = requests.get(url)
text = raw_input.text
print(text)
