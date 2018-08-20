from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.example.com").text
soup = BeautifulSoup(html, 'html5lib')

p0 = soup.find('p')
text = soup.find('p')
text = soup.p.text
words = soup.p.text.split()
id = soup.p['id']
id2 = soup.p.get('id')

all_paragraphs = soup.find_all('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]

spans_inside_divs = [span
                     for div in soup('div')
                     for span in div('span')]
