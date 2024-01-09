from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    task_id: int
    title: str
    description: Optional[str] = None
    date_ = datetime
    status: bool = False

