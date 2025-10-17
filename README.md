# PydSQL

[![PyPI version](https://badge.fury.io/py/pydsql.svg)](https://badge.fury.io/py/pydsql)  
A lightweight Python utility to generate SQL `CREATE TABLE` statements directly from your Pydantic models.

---

### What is PydSQL?

PydSQL is a simple, focused developer tool that bridges the gap between your Pydantic data models and your SQL database schema. It reads your Pydantic model and automatically generates a corresponding `CREATE TABLE` statement, saving you time and preventing manual errors.

It is **not** a full ORM like SQLAlchemy. It's a "get out of the way" utility for developers who want to write their own SQL queries but hate writing boilerplate schema definitions.

### Why Does it Exist?

While working with powerful tools like SQLAlchemy, I realized that for many smaller projects or quick prototypes, a full ORM can be overkill. The setup is complex, and it hides the underlying SQL.

However, without an ORM, I was back to manually writing `CREATE TABLE` statements, which was repetitive and error-prone. It was easy for my database schema to drift out of sync with my Pydantic models.

PydSQL was built to solve this specific pain point. It automates the most tedious part of setting up a database—schema creation—while leaving you in full control to write your own SQL.

### Installation

You can now install PydSQL directly from PyPI:

```bash
pip install pydsql
