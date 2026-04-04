from flask import Blueprint
from app.models import Product


index_bp = Blueprint("main", __name__)


@index_bp.route("/")
def index():
    products = Product.query.all()

    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
        }
        for p in products
    ]
