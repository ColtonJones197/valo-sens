import requests
from bs4 import BeautifulSoup

request_url = 'https://prosettings.net/valorant-pro-settings-gear-list/'

def get_first_player_line(url: str):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, features='html.parser')
	entries = []
	for row in soup.find_all("tr"):
		new_entry = []
		for col in row.find_all("td"):
			new_entry.append(col.string)
		entries.append(new_entry)
	print(f'found {len(entries)} entries')
	

if __name__ == '__main__':
	get_first_player_line(request_url)