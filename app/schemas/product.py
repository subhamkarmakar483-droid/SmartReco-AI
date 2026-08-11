from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    category: str
    price: float


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    category: str
    price: float


    model_config = {
        "from_attributes": True
    }
