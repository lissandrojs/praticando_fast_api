from datetime import datetime
from sqlalchemy import String, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api_sports_training_center.contrib.models import BaseModel


class TrainerCenterModel(BaseModel):
    __tablename__ = 'training_center'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String,nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    owner: Mapped[str] = mapped_column(String, nullable=False)
    training_center: Mapped['AthleteModel'] = relationship(back_populates='training_center')
    created_at: Mapped[datetime] =  mapped_column(DateTime)