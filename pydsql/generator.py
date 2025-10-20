from datetime import date
from typing import Type
from pydantic import BaseModel

from typing import get_origin, get_args, Optional, Union
from pydsql.column import Column


def generate_sql(model: Type[BaseModel]) -> str:
    """
    Generate a SQL CREATE TABLE statement from a Pydantic model.

    Args:
        model (Type[BaseModel]): A Pydantic model class.

    Returns:
        str: SQL CREATE TABLE statement.
    """
    table_name = model.__name__.lower()
    fields = model.model_fields
    
    type_mapping = {
        int: "INTEGER",
        str: "TEXT",
        float: "REAL",
        bool: "BOOLEAN",
        date: "DATE",
    }

    columns = []
    for field_name, field in fields.items():

        # Creates instance of a column builder
        column = Column(field_name,field)

        # Applies the check for NULL and UNIQUE
        column.apply_nullability()
        column.apply_unique()
        
        # appends the column string made by .build()
        columns.append( column.build() )

    columns_sql = ",\n    ".join(columns)
    sql = f"CREATE TABLE {table_name} (\n    {columns_sql}\n);"
    return sql


def generate_create_table_statement(model: Type[BaseModel]) -> str:
    """
    Generate a SQL CREATE TABLE statement from a Pydantic model.
    Alias for generate_sql for better clarity.
    """
    return generate_sql(model)
