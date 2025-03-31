
## **Backend: `backend/README.md`**  
```markdown
# Flight Booking API (FastAPI)

## 📌 Overview
This is a FastAPI-based backend for searching and booking flights using the Duffel API.

## 🏗 Project Structure
```
backend/
│── api/
│   ├── flight_search.py      # Search flights API
│   ├── flight_booking.py     # Book flights API
│   ├── __init__.py
│── duffel_helper.py          # Helper functions for API calls
│── __init__.py
main.py                        # FastAPI entry point
```

## ⚡ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone <repo-url>
cd backend
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install fastapi uvicorn httpx python-dotenv
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and add:
```ini
DUFFEL_ACCESS_TOKEN=your_duffel_api_key
```

### **5️⃣ Run the Server**
```bash
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## 🚀 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET`  | `/flights/search` | Search for flights |
| `POST` | `/bookings/book` | Book a flight |

### **Swagger UI for API Documentation**
Visit `http://127.0.0.1:8000/docs` to test the endpoints.

## 🛠 Example API Calls
### **1️⃣ Search Flights**
```bash
curl "http://127.0.0.1:8000/flights/search?origin=DEL&destination=LHR&departure_date=2024-05-01&max_price=5000"
```

### **2️⃣ Book a Flight**
```bash
curl -X 'POST' 'http://127.0.0.1:8000/bookings/book' \
     -H 'Content-Type: application/json' \
     -d '{"flight_id": "abc123", "passenger_name": "John Doe", "email": "john@example.com"}'
```

## 📜 License
This project is for educational purposes only.
```

