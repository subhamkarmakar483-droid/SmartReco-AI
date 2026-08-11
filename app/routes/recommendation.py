from fastapi import APIRouter, Depends

from app.db.database import SessionLocal
from app.models.user import User
from app.dependencies.auth import get_current_user
from app.agent.recommender import get_recommendation_products
from app.services.mesh import generate_recommendation


router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"]
)


@router.get("/")
def get_recommendation(
    current_user: User = Depends(get_current_user)
):
    db = SessionLocal()

    try:
        # Get products based on the user's latest behavior
        products = get_recommendation_products(
            db,
            current_user.id
        )

        # If the user has no behavior yet
        if not products:
            return {
                "message": "No recommendations available yet."
            }

        # Convert products into text for the AI
        product_text = "\n".join(
            [
                f"- {product.name} | Category: {product.category} | Price: ₹{product.price}"
                for product in products
            ]
        )

        # Prompt sent to Mesh AI
        prompt = f"""
You are SmartReco, a product recommendation agent.

The user recently interacted with a product in the {products[0].category} category.

Here are the available products:

{product_text}

Choose the best 1 or 2 products from ONLY this list.

Write exactly ONE short sentence.

Mention the recommended product name and briefly explain why it is relevant.

Do NOT:
- invent products
- mention products outside the list
- use bullet points
- use greetings
- use quotes
- add extra explanation
- say "Good luck with your purchase"

Keep the response under 25 words.
"""

        # Generate AI recommendation through Mesh API
        recommendation = generate_recommendation(prompt)

        return {
            "recommendation": recommendation,
            "products": products
        }

    finally:
        db.close()

