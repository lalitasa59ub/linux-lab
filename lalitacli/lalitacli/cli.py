import click

from bs4 import BeautifulSoup
import requests
import json

from PIL import Image
from StringIO import StringIO

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False)
def main(name, as_cowboy):
	"""My Tool does one thing, and one thing well."""
	#greet = 'Howdy' if as_cowboy else 'Hello'
    	#click.echo('{0}, {1}.'.format(greet, name))
    	#r = getURL('Mr Incredible')
	url='https://www.smartphonetabletthai.com/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5-%E0%B8%AE%E0%B8%B5%E0%B9%82%E0%B8%A3%E0%B9%88-rov-%E0%B8%97%E0%B8%B8%E0%B8%81%E0%B8%95%E0%B8%B1%E0%B8%A7/'
	html=requests.get(url)
	b=BeautifulSoup(html.content,'html.parser')
	search=b.find_all('img')
	for x in range(3,len(search)-14):
		if name.lower() in search[x]['alt'].lower() :
			url=search[x]['src']
			break;
		
	req=requests.get(url)
	img=Image.open(StringIO(req.content))
	img.show()

