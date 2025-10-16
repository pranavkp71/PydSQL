from datetime import date


def generate_sql(model):
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
    sql = f"CREATE TABLE {table_name} (\n   {columns_sql}\n);"

    return sql
