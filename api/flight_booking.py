# backend/api/flight_booking.py

from fastapi import APIRouter, HTTPException
from duffel_helper import book_flight

router = APIRouter()

@router.post("/book")
async def book(
    flight_id: str,
    passenger_name: str,
    email: str
):
    try:
        booking_info = await book_flight(flight_id, passenger_name, email)
        return booking_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
