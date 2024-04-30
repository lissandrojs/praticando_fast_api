from datetime import datetime
from sqlalchemy import  Float, String, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from api_sports_training_center.contrib.models import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String,nullable=False)
    category: Mapped['AthleteModel'] = relationship(back_populates='category')
    created_at: Mapped[datetime] =  mapped_column(DateTime)