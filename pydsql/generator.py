from datetime import date
from typing import Type
from pydantic import BaseModel


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
        python_type = field.annotation
        sql_type = type_mapping.get(python_type, "TEXT")
        column_def = f"{field_name} {sql_type}"
        columns.append(column_def)

    columns_sql = ",\n    ".join(columns)
    sql = f"CREATE TABLE {table_name} (\n    {columns_sql}\n);"
    return sql


def generate_create_table_statement(model: Type[BaseModel]) -> str:
    """
    Generate a SQL CREATE TABLE statement from a Pydantic model.
    Alias for generate_sql for better clarity.
    """
    return generate_sql(model)
