from pydantic import BaseModel
from datetime import date
from pydsql.generator import generate_sql
from typing import Optional, Annotated


def test_generate_sql_with_constrains():
    class Product(BaseModel):
        product_id: int 
        name: str 
        aftername: Optional[str]
        email: Annotated[str,"UNIQUE"] 
        price: float
        launch_date: date
        is_available: bool

    expected_sql = (
        "CREATE TABLE product (\n"
        "    product_id INTEGER NOT NULL,\n"
        "    name TEXT NOT NULL,\n"
        "    aftername TEXT,\n"
        "    email TEXT NOT NULL UNIQUE,\n"
        "    price REAL NOT NULL,\n"
        "    launch_date DATE NOT NULL,\n"
        "    is_available BOOLEAN NOT NULL\n"
        ");"
    )

    actual_sql = generate_sql(Product)
   
    assert actual_sql == expected_sql
    
test_generate_sql_with_constrains()