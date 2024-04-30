from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat


class AthleteSchema(BaseModel):
    name: Annotated[str, Field(description="Nome do atleta", examples="Jose", max_length=100)]
    cpf: Annotated[str, Field(description="Numero do cpf", examples="11111111111", max_length=11)]
    age: Annotated[int, Field(description="Idade do atleta", examples=25)]
    weight: Annotated[PositiveFloat, Field(description="Peso do atleta", examples=68.5)]
    height: Annotated[PositiveFloat, Field(description="Altura do atleta", examples=1.78)]
    sex: Annotated[str, Field(description="Sexo do atleta", examples="M")]
