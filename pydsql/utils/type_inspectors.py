
from typing import get_origin, get_args, Optional, Union

class FieldInspector:

    @classmethod
    def is_nullable(cls,annotation):
        return (
            get_origin(annotation) in (Union, Optional)
            and type(None) in get_args(annotation)
        )
    @classmethod
    def extract_base_type(cls,annotation):
        origin = get_origin(annotation)
        args = get_args(annotation)

        if origin in (Union, Optional):
            for arg in args:
                if arg is not type(None):
                    return arg
        return annotation
    
    @classmethod
    def is_unique (cls,field):
        metadata = getattr(field, "metadata", [])
        return "UNIQUE" in metadata
       
    

