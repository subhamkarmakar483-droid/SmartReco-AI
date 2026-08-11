from pydantic import BaseModel


class BehaviorCreate(BaseModel):
    product_id: int
    event_type: str

class BehaviorResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    event_type: str

    model_config = {
        "from_attributes": True
    }