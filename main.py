

from fastapi import FastAPI
from api.flight_search import router as flight_search_router
from api.flight_booking import router as flight_booking_router

app = FastAPI()


app.include_router(flight_search_router, prefix="/flights")
app.include_router(flight_booking_router, prefix="/flights")
