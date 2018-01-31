from bs4 import BeautifulSoup
import requests

search = input('Search For: ') #for user to input text for search
params = {'q': search} #We put thqt into a search variable
r = requests.get('https://www.bing.com/search', params=params) #We make a request object

soup = BeautifulSoup(r.text, 'html.parser') #We build a soup
results = soup.find('ol', {'id': 'b_results'}) #We search through the soup
links = results.findAll('li', {'class': 'b_algo'}) #We search inside the reszlts

for item in links:
    item_text = item.find('a').text
    item_href = item.find('a').attrs['href'] #attribute called href

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print('Summary:', item.find('a').parent.parent.find('p').text)

        #children = item.find('h2')
        #print('Next sibling of the h2:', children.next_sibling)