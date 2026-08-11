from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from app.models.behavior import UserBehavior
from app.schemas.behavior import BehaviorCreate, BehaviorResponse
from app.models.user import User
from app.dependencies.auth import get_current_user


router = APIRouter(
    prefix="/behavior",
    tags=["Behavior"]
)


@router.post("/",response_model=BehaviorResponse)
def create_behavior(
    behavior: BehaviorCreate,
    current_user: User = Depends(get_current_user)
):
    db = SessionLocal()

    new_behavior = UserBehavior(
        user_id=current_user.id,
        product_id=behavior.product_id,
        event_type=behavior.event_type
    )

    db.add(new_behavior)
    db.commit()
    db.refresh(new_behavior)

    return new_behavior