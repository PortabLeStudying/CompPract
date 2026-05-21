import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

first_quote = soup.find('span', class_='text').text
first_author = soup.find('small', class_='author').text

print(f'Цитата: "{first_quote}", Автор: {first_author}')