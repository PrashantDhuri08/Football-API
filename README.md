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


# 🚀 Running the Project

You can run this FastAPI backend using either **uv** (recommended for reproducible builds) or plain **Python**.

---

## 🛠 Using `uv`

1.  Install [uv](https://github.com/astral-sh/uv):
    ```bash
    pip install uv
    ```
2.  Sync dependencies:
    ```bash
    uv sync
    ```
3.  Run the FastAPI app:
    ```bash
    uv run uvicorn main:app --reload
    ```

---

## Using plain Python

1.  Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
2.  Activate the environment:
    ```bash
    source .venv/bin/activate   # Linux/Mac
    .venv\Scripts\activate      # Windows
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the FastAPI app:
    ```bash
    uvicorn main:app --reload
    ```


    ---
## 📖 Example Usage

### Health Check
```bash
GET /health




