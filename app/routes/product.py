import uuid
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.extensions import db
from app.models import Product


bp = Blueprint("product", __name__)


@bp.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()
    user_id = get_jwt_identity()

    product = Product(
        name=data["name"],
        price=data["price"],
        description=data["description"],
        user_id=user_id,
    )

    db.session.add(product)
    db.session.commit()

    return {"message": "Product created"}, 201


@bp.route("/products", methods=["GET"])
@jwt_required()
def get_my_products():
    user_id = get_jwt_identity()
    products = Product.query.filter_by(user_id=user_id).all()

    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
        }
        for p in products
    ]


@bp.route("/products/<uuid:product_id>", methods=["GET"])
@jwt_required()
def get_product(product_id: uuid.UUID):
    user_id = get_jwt_identity()

    product = Product.query.filter_by(
        id=str(product_id),
        user_id=user_id,
    ).first()

    if not product:
        return {"error": "Not found"}, 404

    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
    }


@bp.route("/products/<uuid:product_id>", methods=["PUT"])
@jwt_required()
def update_product(product_id: uuid.UUID):
    user_id = get_jwt_identity()
    data = request.get_json()

    product = Product.query.filter_by(
        id=str(product_id),
        user_id=user_id,
    ).first()

    if not product:
        return {"error": "Not found"}, 404

    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.description = data.get("description", product.description)

    db.session.commit()

    return {"message": "Updated"}


@bp.route("/products/<uuid:product_id>", methods=["DELETE"])
@jwt_required()
def delete_product(product_id: uuid.UUID):
    user_id = get_jwt_identity()

    product = Product.query.filter_by(
        id=str(product_id),
        user_id=user_id,
    ).first()

    if not product:
        return {"error": "Not found"}, 404

    db.session.delete(product)
    db.session.commit()

    return {"message": "Deleted"}