from fastapi import FastAPI
from backend.routes import interaction_routes
from backend.db.database import init_db

app = FastAPI()

# ✅ DB auto-create on start
init_db()

# ✅ routes
app.include_router(interaction_routes.router)

@app.get("/")
def root():
    return {"message": "AI CRM Backend Running 🚀"}