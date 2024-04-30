from typing import Annotated
from pydantic import BaseModel, Field


class TrainingCenterSchema(BaseModel):
    name: Annotated[str, Field(description="Nome do centro de treinamento", examples="Toca da raposa")]
    address: Annotated[str,Field(description="Endereço do centro de treinamento", examples="Toca da Raposa 2, Rua Adolfo Lippi Fonseca, 250 - Trevo, Belo Horizonte - MG, 31545-170")]
    owner: Annotated[str, Field(description="Nome do dono do centro de treinamento", examples="Pedrinho BH")]