from fastapi import FastAPI
import FakerGenerator
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "End To End MinIO Example"}

@app.get("/FlightPerson")
def createPerson():
    print(FakerGenerator.CreateFakeFlightPerson())
    return json.dumps(str(FakerGenerator.CreateFakeFlightPerson()))