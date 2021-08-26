from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.yellowpages.ca/search/si/1/Restaurants/Toronto+ON"
url1 = "https://www.yellowpages.ca/search/si/1/Stock+Market/Toronto+ON"

page1 = requests.get(url1)

soup = BeautifulSoup(page1.content, 'html.parser')

lists1 = soup.find_all('div', class_="listing_right_section")

with open('StockMarket.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['BusinessName', 'PhoneNumber', 'Address', 'Title']
    thewriter.writerow(header)

    for list1 in lists1:
        businessname = list1.find('a', class_="listing__name--link listing__link jsListingName").text.replace('\n', '')
        PhoneNumber = list1.find('ul', class_="mlr__submenu").text.replace('\n', '')
        address = list1.find('span', class_="listing__address--full").text.replace('\n', '')
        title = list1.find('div', class_="listing__headings__roots").text.replace('\n', '')

        info1 = [businessname, PhoneNumber, address, title]
        thewriter.writerow(info1)



