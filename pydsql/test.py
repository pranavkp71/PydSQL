from pydantic import BaseModel
from datetime import date
from pydsql.generator import generate_sql

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    launch_date: date
    is_available: bool

print(generate_sql(Product))
