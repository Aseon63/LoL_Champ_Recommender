from bs4 import BeautifulSoup
import requests
import random

html = "http://www.op.gg/champion/statistics"

def selector(position):
    position = position.upper()
    url = requests.get(html) #get url info from op.gg
    soup = BeautifulSoup(url.text, "html.parser") #put url into soup
    line_info = soup.find("div",{"class":"l-champion-index-content--side"}).find("table",{"class":"champion-index-table"}).find("tbody",{"class":f"champion-trend-tier-{position}"})
    return line_info

def list_bringer(champion_info):
    rank = champion_info.find("td",{"class":"champion-index-table__cell--rank"}).get_text()
    champion_name = champion_info.find("td",{"class":"champion-index-table__cell--champion"}).find("div",{"class":"champion-index-table__name"}).get_text()
    return {'rank':rank,'champion name':champion_name}

def list_maker(position):
    hi_rank_champs = []
    position = position.upper()
    url = requests.get(html)
    soup = BeautifulSoup(url.text, "html.parser")
    selected_position = selector(position).find_all("tr")
    x = 0
    for selection in selected_position:
        champ_info = list_bringer(selection)
        hi_rank_champs.append(champ_info)
    return hi_rank_champs

def random_choicer(position, ranges):
    ranged_sequence = []
    position = position.upper()
    sequence = list_maker(position)
    sequence_length = len(sequence)
    if ranges > sequence_length:
        ranges = sequence_length
    for r in range(ranges):
        ranged_sequence.append(sequence[r])
    ranged_sequence = random.choice(sequence)
    return ranged_sequence