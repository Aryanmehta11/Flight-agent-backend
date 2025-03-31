import os
import httpx
from dotenv import load_dotenv

load_dotenv()
DUFFEL_TOKEN = os.getenv("DUFFEL_ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {DUFFEL_TOKEN}",
    "Duffel-Version": "v1"
}

# Function to search flights
async def search_flights(origin, destination, date, max_price, preferred_airline=None):
    url = "https://api.duffel.com/air/offer_requests"
    payload = {
        "data": {
            "slices": [{
                "origin": origin,
                "destination": destination,
                "departure_date": date
            }],
            "passengers": [{"type": "adult"}],
            "cabin_class": "economy"
        }
    }

    async with httpx.AsyncClient() as client:
        try:
            print("📤 Sending request to Duffel API...")
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()

            offer_request = response.json()
            offer_request_id = offer_request["data"]["id"]

            offer_url = f"https://api.duffel.com/air/offers?offer_request_id={offer_request_id}"
            offer_response = await client.get(offer_url, headers=headers)
            offer_response.raise_for_status()

            offers = offer_response.json().get("data", [])

            offers = [o for o in offers if float(o["total_amount"]) <= float(max_price)]

            if preferred_airline:
                offers = [o for o in offers if preferred_airline.lower() in o["owner"]["name"].lower()]

            return offers

        except httpx.HTTPStatusError as e:
            print("❌ HTTP Error:", e.response.status_code)
            return []

        except Exception as e:
            print("❌ Unexpected Error:", str(e))
            return []

# Function to simulate flight booking (mock)
async def book_flight(flight_id, passenger_name, email):
    url = "https://api.duffel.com/air/bookings"
    payload = {
        "data": {
            "offer_id": flight_id,
            "passengers": [{"name": passenger_name, "email": email, "type": "adult"}],
            "cabin_class": "economy",
            "payment": {"amount": 1000, "currency": "INR"}  # Simulating a mock payment of 1000 INR
        }
    }

    async with httpx.AsyncClient() as client:
        try:
            print("📤 Sending booking request to Duffel API...")
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()

            booking = response.json()
            booking_reference = booking["data"]["id"]

            print(f"✅ Booking successful. Booking reference: {booking_reference}")

            return {"reference_id": booking_reference}

        except httpx.HTTPStatusError as e:
            print("❌ HTTP Error:", e.response.status_code)
            return {"error": str(e)}

        except Exception as e:
            print("❌ Unexpected Error:", str(e))
            return {"error": str(e)}
