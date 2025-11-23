# Football API

An **API** that provides fixtures, results, and standings for major football leagues.  
This API is designed for developers who want to integrate football data into their apps, dashboards, or services.

---

## Features
- **Health Check Endpoint**  
  - `GET /` → Confirms the API is running.  

- **League Table Endpoint**  
  - `GET /table/{league}` → Returns the standings for the specified league.  
  - Supported leagues :  
    - UEFA Champions League (`ucl`)  
    - UEFA Europa League (`uel`) 
    - La Liga (`laliga`)  
    - Premier League (`PL`)  
    - Bundesliga (`bundesliga`)  
    - Serie A (`seriea`)  

 
 - **League Results Endpoint**  
  - `GET /result/{league}` → Returns the standings for the specified league.  
  - Supported leagues :  
    - UEFA Champions League (`ucl`)  
    - UEFA Europa League (`uel`) 

- **League fixtures Endpoint**  
  - `GET /fixtures/{league}` → Returns the standings for the specified league.  
  - Supported leagues :  
    - UEFA Champions League (`ucl`)  
    - UEFA Europa League (`uel`) 

- **Fixtures & Results**  
  - Upcoming matches include team names, date, and time.  
  - Finished matches include team names and scores.  
  - Unified schema ensures consistent JSON output.

---

## 📖 Example Usage

### Health Check
```bash
GET /health