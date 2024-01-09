import databases
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column


Base = declarative_base()


Base = declarative_base()

class TaskSql(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True)
    title = Column(String(60))
    locality = Column(String(200))
    data = Column(String(20))
    status = Column(String(10))
