from typing import Annotated
from fastapi import Depends

def pagination_params(page: Annotated[int, Depends()] = 1, size: Annotated[int, Depends()] = 10):
    return {"page": page, "size": size}

def get_query_filter(q:str | None = None, pagination:dict = Depends(pagination_params)):
        return {
              "filter": q,
              "offset": (pagination["skip"]),
              "max": pagination["size"]
        }