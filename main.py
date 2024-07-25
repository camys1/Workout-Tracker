import requests
from datetime import datetime
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

GENDER = "female"
WEIGHT_KG = 50
HEIGHT_CM = 1.73
AGE = 20

YOUR_TOKEN = os.getenv("YOUR_TOKEN")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

natural_language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise" 
sheety_endpoint = "https://api.sheety.co/a3d1d00ff36344587c52925e5e164baa/workoutTracking/workouts"

headers = {
    "x-app-id" :APP_ID,
    "x-app-key" : API_KEY
}
query = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=natural_language_endpoint,json=query, headers=headers)
result = response.json()
# print(result)

now = datetime.now()
current_time = now.strftime("%X")
current_day = now.strftime("%x")


for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date":current_day,
            "time":current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_headers = {
"Authorization": f"Bearer {YOUR_TOKEN}"
}

response = requests.post(url=sheety_endpoint, json=sheet_input, headers=bearer_headers)
print(response.text)