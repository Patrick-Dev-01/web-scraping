from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.climatempo.com.br/").content
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

temperatura = soup.find("span", class_="temperature _margin-l-5")
print(temperatura)