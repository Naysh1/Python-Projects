import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/points-table-standings"
headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}

r=requests.get(url,headers=headers).text

soup=BeautifulSoup(r,"html5lib")
# print(soup.prettify())
data={"TEAMS":[],"MATCHES":[],"WON":[],"LOST":[],"TIED":[],"ABANDONEND":[],"POINTS":[],"NRR":[]}
for row in soup.find_all("tr")[1:]:
    cols = row.find_all("td")
    if len(cols) >= 6: 
        teams=data["TEAMS"].append(cols[0].text)
        matches=data["MATCHES"].append(cols[1].text)
        won=data["WON"].append(cols[2].text)
        lost=data["LOST"].append(cols[3].text)
        tied=data["TIED"].append(cols[4].text)
        abnd=data["ABANDONEND"].append(cols[5].text)
        pts=data["POINTS"].append(cols[6].text)
        nrr=data["NRR"].append(cols[7].text)

df=pd.DataFrame(data)
df_2=pd.DataFrame(df.iloc[0:10,:])
def remove_digits_from_string(s):
    return ''.join(char for char in s if not char.isdigit())
# Apply the function to the DataFrame column
df_2['TEAMS'] = df_2['TEAMS'].apply(lambda x: remove_digits_from_string(x))
df_2.index = pd.RangeIndex(start=1, stop=len(df_2) + 1)
df_2 = df_2.rename_axis('SN')
df_2.to_csv("table_standing.csv")
print(df_2)