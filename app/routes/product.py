from fastapi import APIRouter
from app.db.database import SessionLocal
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/",response_model=ProductResponse)
def craete_product(product: ProductCreate):
    db = SessionLocal()


    new_product = Product(
        name=product.name,
        description=product.description,
        category=product.category,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.get("/", response_model=list[ProductResponse])
def get_products():
    db = SessionLocal()


    products = db.query(Product).all()

    return products
