from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os, requests
from dotenv import load_dotenv
from backend.symptoms import SYMPTOM_DOSHA_MAP

load_dotenv("env.env")
GROK_API_KEY = os.getenv("GROK_API_KEY")
API_URL = "https://api.x.ai/v1/chat/completions"

app = FastAPI()

class SymptomsInput(BaseModel):
    name: str
    age: int
    gender: str
    symptoms: list

@app.post("/diet-plan")
def diet_plan(data: SymptomsInput):
    dosha_count = {"Vata": 0, "Pitta": 0, "Kapha": 0}
    for s in data.symptoms:
        if s in SYMPTOM_DOSHA_MAP:
            dosha_count[SYMPTOM_DOSHA_MAP[s]] += 1
    dominant_dosha = max(dosha_count, key=dosha_count.get)

    prompt = f"""
    Patient Info:
    Name: {data.name}, Age: {data.age}, Gender: {data.gender}
    Symptoms: {', '.join(data.symptoms)}
    Dominant Dosha: {dominant_dosha}

    Based on Ayurveda, generate:
    1. A JSON with keys: dosha, plan (Breakfast/Lunch/Dinner with items+calories), precautions.
    2. Keep response strictly JSON.
    """.strip()

    headers = {"Authorization": f"Bearer {GROK_API_KEY}", "Content-Type": "application/json"}
    body = {
        "model": "grok-4-latest",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.4,
        "stream": False
    }

    response = requests.post(API_URL, headers=headers, json=body)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Grok API error: {response.text}")

    try:
        content = response.json()["choices"][0]["message"]["content"]
        return eval(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse Grok response: {str(e)}")