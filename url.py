from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.google.com").text
soup = BeautifulSoup(html, 'html5lib')

head = soup.find('head')
first_part = soup.head.text
first_part_words = first_part.head.split()

all_paragraphs = soup.find_all('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]
print(paragraphs_with_ids)