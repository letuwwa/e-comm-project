import uuid6
from .extensions import db
from datetime import datetime, UTC
from sqlalchemy.dialects.postgresql.base import UUID


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid6.uuid7,
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )


class User(BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Product(BaseModel):
    __tablename__ = 'products'

    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)