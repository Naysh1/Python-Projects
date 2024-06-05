import requests
url="https://www.espncricinfo.com/records/trophy/team-match-results/indian-premier-league-117"

def fecthAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path,'w',encoding='utf-8') as f:
        f.write(r.text)

fecthAndSaveToFile(url,'ipl.html')