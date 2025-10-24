from datetime import date
from .utils.type_inspectors import FieldInspector

class Column (FieldInspector):
    def __init__(self,name,field):
       
        self.name = name
        self.annotation = field.annotation
        self.python_type =  self.extract_base_type(field.annotation)
        self.required = not self.is_nullable(field.annotation)
        self.unique = self.is_unique(field)
        self.sql_parts = [self.map_type()]
    
    
    
    def map_type(self):
        field = self.annotation
        mapping = {
            int: "INTEGER",
            str: "TEXT",
            float: "REAL",
            bool: "BOOLEAN",
            date: "DATE",
        }
        return mapping.get(self.annotation,"TEXT")
    
    def apply_nullability(self):
        if self.required:
            return self.sql_parts.append("NOT NULL")
        return self
    
    def apply_unique(self):
        if self.unique:
            return self.sql_parts.append("UNIQUE")
        return self
    
    def build(self):
        return f"{self.name} " + " ".join(self.sql_parts)
    

