# to build app
from fastapi import FastAPI#, File, UploadFile
# allows web team access to app
from fastapi.middleware.cors import CORSMiddleware
# allows you to create a class to structure POST input
#from pydantic import BaseModel
# allows for html rendering
from fastapi.responses import HTMLResponse
# for data handling
import pandas as pd

app = FastAPI()

# CORS - Cross-Origin Resource Sharing
# Gives Web Team Access to API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
  """
  Sauti Market Monitor API  
  Verifies the API is deployed, and links to the docs.
  """
  return HTMLResponse("""
  <h1>Sauti Market Monitor</h1>
  <p>Go to <a href="/docs">/docs</a> for documentation.</p>
  """)

@app.get("/qc_wholesale")
async def qc_wholesale():
  qc_ws = pd.read_csv("qc_wholesale.csv")
  qc_ws = qc_ws.to_json()
  return qc_ws