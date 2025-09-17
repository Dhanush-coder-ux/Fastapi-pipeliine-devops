from sqlalchemy import Column,Integer,String,DateTime
from database.main import BASE

class AddToDo(BASE):
    __tablename__ = 'add_todo'
    id = Column(String,autoincrement=False,primary_key=True)
    data = Column(String,nullable=False)
    date_time = Column(DateTime(timezone=True),nullable=False)
    

