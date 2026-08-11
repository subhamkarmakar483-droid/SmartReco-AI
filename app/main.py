from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.routes.behavior import router as behavior_router
from app.routes.product import router as product_router
from app.routes.recommendation import router as recommendation_router

app = FastAPI(
    title="SmartReco AI",
    description="Behavioral Recommendation Engine",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to SmartReco AI!"
    }

app.include_router(behavior_router)
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(recommendation_router)
