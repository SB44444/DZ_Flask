import datetime
from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str = Field(max_length=60, min_length=1)
    description: str = Field(max_length=200, min_length=1)
    date: str = Field(max_length=20)
    status: str = Field(max_length=10)


class TaskOut(TaskIn):
    task_id: int
