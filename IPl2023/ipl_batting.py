import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.espncricinfo.com/records/tournament/batting-most-runs-career/indian-premier-league-2023-15129"
headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}

r = requests.get(url, headers=headers).text

soup = BeautifulSoup(r, "html5lib")
keys = ['Player', 'Span', 'Mat', 'Inns', 'NO', 'Runs', 'HS', 'Ave', 'BF', 'SR', '100', '50', '0', '4s', '6s']
player_info = {key: [] for key in keys}
seen_players = set()

for row in soup.find_all("tr")[1:]:
    cols = row.find_all("td")

    if cols and len(cols) >= 13:
        player_name = cols[0].text.strip()
        if player_name not in seen_players:
            seen_players.add(player_name)
            for i, j in enumerate(keys):
                player_data = cols[i].text.strip()
                player_info[j].append(player_data)
df=pd.DataFrame(player_info)
df.to_csv("ipl_batting.csv",index=False)
print(df)