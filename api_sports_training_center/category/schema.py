from typing import Annotated
from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    name : Annotated[str, Field(description="Nome da categoria", examples="Skate")]
