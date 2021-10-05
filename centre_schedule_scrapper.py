import requests
from bs4 import BeautifulSoup

def scrape():
	URL = 'https://kanpurnagar.nic.in/document-category/vaccine-schedule/'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')
	table = soup.find("div","distTableContent")
	tbody = table.find("tbody")
	table_row = tbody.find("tr")
	link_row = table_row.find("a")
	link = link_row.get("href")
	td = table_row.find_all("td")
	date = td[1].getText()
	return [link,date]
if __name__ == '__main__':
	print(scrape())