from app.models.product import Product
from app.models.behavior import UserBehavior


def get_recommendation_products(db, user_id: int):

    behaviors = (
        db.query(UserBehavior)
        .filter(UserBehavior.user_id == user_id)
        .order_by(UserBehavior.created_at.desc())
        .all()
    )

    if not behaviors:
        return []

    latest_behavior = behaviors[0]

    current_product = (
        db.query(Product)
        .filter(Product.id == latest_behavior.product_id)
        .first()
    )

    if not current_product:
        return []

    products = (
        db.query(Product)
        .filter(
            Product.category == current_product.category,
            Product.id != current_product.id
        )
        .limit(5)
        .all()
    )

    # Remove duplicate product names
    unique_products = []
    seen_names = set()

    for product in products:
        if product.name not in seen_names:
            unique_products.append(product)
            seen_names.add(product.name)

    return unique_products