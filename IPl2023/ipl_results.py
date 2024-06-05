import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.espncricinfo.com/records/trophy/team-match-results/indian-premier-league-117"
headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}

r=requests.get(url,headers=headers).text

soup=BeautifulSoup(r,"html5lib")
# print(soup.prettify())

href_data=[]
data={"Team_1":[],"Team_2":[],"Winner":[],"Margin":[],"Ground":[],"Match_Date":[],"Scorecard":[]}

for row in soup.find_all("tr")[1:]:
    cols = row.find_all("td")
    
    # Extract data from each <td> tag
    if len(cols) >= 6: 
       
        team1=data["Team_1"].append(cols[0].text)
        team2=data["Team_2"].append(cols[1].text)
        winner=data["Winner"].append(cols[2].text)
        margin=data["Margin"].append(cols[3].text)
        ground=data["Ground"].append(cols[4].text)
        date=data["Match_Date"].append(cols[5].text)
        scorecard=(cols[6].find("a"))
        if scorecard:  # Check if <a> tag exists
            href = scorecard.get("href")  # Get the value of href attribute
            data["Scorecard"].append(href)

df=pd.DataFrame.from_dict(data)
subset = df[df['Match_Date']=="Apr 1, 2023"]#142
subset = df[df['Match_Date']=="May 28-29, 2023"]#63
# print(subset)
# Using Indexing
subset = df.iloc[71:145, :]

new_data =pd.DataFrame(subset)
new_data["Scorecard"]="https://www.espncricinfo.com"+new_data["Scorecard"]
new_data.to_excel("ipl_results.xlsx",index=False)
new_data.to_csv("ipl_results.csv",index=False)
print(new_data)