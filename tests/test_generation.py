from pydantic import BaseModel
from datetime import date
from pydsql.generator import generate_sql


def test_basic_product_model():
    class Product(BaseModel):
        product_id: int
        name: str
        price: float
        launch_date: date
        is_available: bool

    expected_sql = (
        "CREATE TABLE product (\n"
        "   product_id INTEGER,\n"
        "    name TEXT,\n"
        "    price REAL,\n"
        "    launch_date DATE,\n"
        "    is_available BOOLEAN\n"
        ");"
    )

    actual_sql = generate_sql(Product)

    assert actual_sql == expected_sql
