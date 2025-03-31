from fastapi import APIRouter, Query, HTTPException
from duffel_helper import search_flights 

router = APIRouter()

@router.get("/search")
async def search(
    origin: str = Query(...),
    destination: str = Query(...),
    departure_date: str = Query(...),  # format: YYYY-MM-DD
    max_price: int = Query(5000),
    preferred_airline: str = Query(None),
    cabin_class: str = Query("economy"),  # options: economy, business, etc.
    currency: str = Query("INR")
):
    try:
        flights = await search_flights(
            origin,
            destination,
            departure_date,
            max_price,
            preferred_airline,
            cabin_class,
            currency
        )
        return {"flights": flights}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

