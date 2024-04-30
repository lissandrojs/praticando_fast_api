from datetime import datetime
from sqlalchemy import  Float, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api_sports_training_center.contrib.models import BaseModel


class AthleteModel(BaseModel):
    __tablename__ = 'athletes'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String,nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    age: Mapped[int] = mapped_column(String(25),nullable=False)
    weight: Mapped[float] = mapped_column(Float,nullable=False)
    height: Mapped[float] = mapped_column(Float,nullable=False)
    sex: Mapped[str] = mapped_column(String(1),nullable=False)
    category: Mapped['CategoryModel'] = relationship(back_populates='athlete')
    caregory_id: Mapped[int] = mapped_column(ForeignKey('categories.pk_id'))
    training_center: Mapped['TrainerCenterModel'] = relationship(back_populates='training_center')
    training_center_id: Mapped[int] = mapped_column(ForeignKey('training_center.pk_id'))
    created_at: Mapped[datetime] =  mapped_column(DateTime)