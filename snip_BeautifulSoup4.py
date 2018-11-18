# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

s_html ="blbalbalbalbalba"
soup = BeautifulSoup(s_html, 'html.parser')

def get_link(soup):	
	for link in soup.find_all('a'):
    print(link.get('href'))

    # Before get('href')
	# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,

	# After get('href')
	# http://example.com/lacie

def Get_text_from_html(soup):
	soup.get_text()