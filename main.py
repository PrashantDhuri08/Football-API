from fastapi import FastAPI
from bs4 import BeautifulSoup
import lxml
import re
import requests
from fastapi.responses import JSONResponse
from enum import Enum

class League(Enum):
    LALIGA = "laliga-10"
    UCL = "uefa-champions-league-5"
    PL = "premier-league-9"
    SERIEA = "serie-a-13"
    UEL = "uefa-europa-league-7"
    BUNDESLIGA = "bundesliga-1"

app = FastAPI()

@app.get("/")
def health():
    return {"response":"This is a football api for getting fixtures, results and standings of various leagues"}

# Works for every league
@app.get("/table/{league}")
def table(league :str):

    lname = League[league.upper()].value

    link = f"https://onefootball.com/en/competition/{lname}/table"

    page = requests.get(link).text
    source = BeautifulSoup(page, "lxml")
    element = source.find_all("a", class_= "Standing_standings__rowGrid__45OOd")
    table = []

    for teams in element:
        tt= teams.get_text(separator=" | ").strip()

        table.append(tt)

    
    standings = []
    for row in table:
        parts = [p.strip() for p in row.split('|')]
        standings.append({
            "position": int(parts[0]),
            "team": parts[1],
            "played": int(parts[2]),
            "wins": int(parts[3]),
            "draws": int(parts[4]),
            "losses": int(parts[5]),
            "goal_diff": int(parts[6]),
            "points": int(parts[7])
        })


    
    return JSONResponse({"table": standings})

#only for UCL
@app.get("/fixtures/{league}")
def fixtures(league: str):
    
    lname = League[league.upper()].value
    link = f"https://onefootball.com/en/competition/{lname}/fixtures"

    # if league == "ucl":
    #     link = "https://onefootball.com/en/competition/uefa-champions-league-5/fixtures"
    # elif league == "laliga":    
    #     link = "https://onefootball.com/en/competition/laliga-10/fixtures"
    # else:
    #     return "Invalid parameters"    

    source = requests.get(link).text

    page = BeautifulSoup(source, "lxml")

    fix= page.find_all("a", class_="MatchCard_matchCard__iOv4G")

    fixtures = []
    for match in fix:
        fixture = match.get_text(separator="|").strip()  
        fixtures.append(fixture)

    structuredfixture = []
    for row in fixtures:
        parts = [p.strip() for p in row.split('|')]
        structuredfixture.append({
            "Team1": parts[0],
            "Team2": parts[1],
            "Date": parts[2],
            "Time": parts[3]
        })


    return JSONResponse({"fixtures": structuredfixture})



# Currently only works for UCL 
@app.get("/result/{league}")
def results(league:str):

    # league_para= str(getleaguename(league))

    league_para = League[league.upper()].value

    link = f"https://onefootball.com/en/competition/{league_para}/results"


    page= requests.get(link).text

    source = BeautifulSoup(page, "lxml")

    classname = "MatchCard_matchCard__iOv4G"

    results = source.find_all("a", class_=classname)


    resultlist = []

    for i in results:
        mm= i.get_text(separator=" | ").strip()

        resultlist.append(mm)


    structuredres= []

    for row in resultlist:
        parts =[p.strip() for p in row.split('|')]
        structuredres.append(
            {
                parts[0] : int(parts[1]),
                parts[2] : int(parts[3]),
                "Date": parts[4]
            }
        )

    # return JSONResponse({"result":resultlist})
    return JSONResponse({"result":structuredres})



    
