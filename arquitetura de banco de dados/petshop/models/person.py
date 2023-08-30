# faz as mesmas coisas que o sor mostrou na aula coloque o nome da coluna (id) e os tipos atribuidos (not null, int)
from models import base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTERGER, BIGINT, MEDIUMTEXT, ForeignKey

class Person(base):
    __tableaname__ = 'Person'
    id: Mapped[BIGINT] = mapped_column(INTERGER, nullable=False, primary_key=True, autoincrement= True)
    
