from fastapi import FastAPI, Path, Query, HTTPException, status, Form, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from random import randint
import pandas as pd
from openpyxl import load_workbook
import datetime as dt



QUOTE_IDS_TRACKER = []

templates = Jinja2Templates(directory="templates/")


def generate_random_number(data):
    min_quote_id = data.id.min()
    max_quote_id = data.id.max()
    random_id = randint(min_quote_id, max_quote_id)
    return random_id

def create_report():
    current_date_time = str(dt.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    spreadsheet_name = "quotes_api_report_" + current_date_time + ".xlsx"

    pd.Series(QUOTE_IDS_TRACKER).value_counts().to_excel(spreadsheet_name) 
    wb = load_workbook(spreadsheet_name)
    ws = wb.active
    ws["A1"] = "Quote ID"
    ws["B1"] = "Count"
    wb.save(filename = spreadsheet_name)
    QUOTE_IDS_TRACKER.clear()


#################################################
    
app = FastAPI()
    
@app.get("/quote/random", response_class=JSONResponse)
def get_random_quote(request: Request):
    """
    Generates a random quote ID and displays it along with the quote and the author
    """
    json_quotes_data = pd.read_json("quotes.json")
    json_authors_data = pd.read_json("authors.json")

    random_id = generate_random_number(json_quotes_data)

    resulted_quote = json_quotes_data.loc[(json_quotes_data.id == random_id)]

    resulted_quote_id = str(resulted_quote.id.values[0])
    QUOTE_IDS_TRACKER.append(resulted_quote_id)
    resulted_quote = str(resulted_quote.quote.values[0])

    for index, qoute_ids_lists in enumerate(json_authors_data["quoteIds"]):
        if random_id in qoute_ids_lists:
            resulted_author = str(json_authors_data.iloc[index].author)
            
    if len(QUOTE_IDS_TRACKER) == 100:
        create_report()
        
    return templates.TemplateResponse("index.html", {"request": request, "quoteId": resulted_quote_id, "quote": resulted_quote, "author": resulted_author})
