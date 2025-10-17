## PydSQL

[![PyPI version](https://img.shields.io/pypi/v/pydsql.svg)](https://pypi.org/project/pydsql/)
[![Python versions](https://img.shields.io/pypi/pyversions/pydsql.svg)](https://pypi.org/project/pydsql/)
[![Build](https://img.shields.io/github/actions/workflow/status/pranavkp71/PydSQL/ci.yml?branch=main)](https://github.com/pranavkp71/PydSQL/actions)
[![Coverage](https://img.shields.io/codecov/c/github/pranavkp71/PydSQL)](https://codecov.io/gh/pranavkp71/PydSQL)
[![Contributing](https://img.shields.io/pypi/l/pydsql.svg)](./CONTRIBUTING.md)
[![License](https://img.shields.io/pypi/l/pydsql.svg)](./LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pydsql.svg)](https://pypi.org/project/pydsql/)

A lightweight Python utility to generate SQL `CREATE TABLE` statements directly from your Pydantic models.

---

## What is PydSQL?

PydSQL is a focused developer tool that bridges the gap between your **Pydantic data models** and your **SQL database schema**. It reads your Pydantic model and automatically generates a corresponding `CREATE TABLE` statement, saving time and preventing manual errors.

PydSQL is not a full ORM like SQLAlchemy. It’s a lightweight utility for developers who want to write their own SQL but hate repetitive schema definitions.

---

## Why Does it Exist?

While ORMs are powerful, they can be overkill for small projects or prototypes. Without an ORM, manually writing `CREATE TABLE` statements is error-prone and can drift out of sync with Pydantic models. PydSQL automates this tedious part while leaving you in full control.

---

## Installation

Install directly from PyPI:

```bash
pip install pydsql
```

Or install from source:

```bash
git clone https://github.com/pranavkp71/PydSQL.git
cd PydSQL
pip install .
```

---

## Usage

### Single model

```python
from pydantic import BaseModel
from pydsql.generator import generate_create_table_statement
from datetime import date

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    launch_date: date
    is_available: bool

sql = generate_create_table_statement(Product)
print(sql)
```

### Output

```sql
CREATE TABLE product (
    product_id INTEGER,
    name TEXT,
    price REAL,
    launch_date DATE,
    is_available BOOLEAN
);
```

### Multiple models

```python
from pydsql.generator import generate_create_table_statement

# Assuming Product and AnotherModel are defined Pydantic models
models = [Product, AnotherModel]

for model in models:
    print(generate_create_table_statement(model))
```

---

## Features

- **Automatic schema generation**: Convert Pydantic models to SQL `CREATE TABLE` statements.
- **Basic types supported**: `int`, `str`, `float`, `bool`, `date`.
- **Lightweight and ORM-free**: Designed for developers who prefer writing SQL.
- **Pydantic v2 compatible**: Works with modern Pydantic versions.

---

## Contributing

Contributions are welcome! Please see [`CONTRIBUTING.md`](./CONTRIBUTING.md) for setup, testing, linting, and pull request guidelines.

---

## License

MIT
