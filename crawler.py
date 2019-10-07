
import requests
from bs4 import BeautifulSoup

def get_single_item_data(item_url):
    #get the source code of the web page
    source_code = requests.get(item_url)
    #get only the links , images znd other html tag
    plain_text = source_code.text
    #allows for easy modification of the result gotten from the webpage
    soup = BeautifulSoup(plain_text)
    #get all h1
    for item_name in soup.findAll('h1'):
        print("Title: ")
        print(item_name.string)
        print("\n")
    #get all the p tags in the web page
    for item_content in soup.findAll('p'):
        print(item_content.string)

url = ''
get_single_item_data(url)