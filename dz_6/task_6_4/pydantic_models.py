from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str = Field()
    description: str | None = Field(default=None)
    status: bool = Field(default=False)


class TaskSql(TaskIn):
    id: int
