from asyncio import Task
import fastapi
import sqlalchemy
from sqlalchemy import select, insert, update, delete
import pydantic_models
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import typing
from contextlib import asynccontextmanager
from sqlalchemy_models import TaskSql, Column
from fastapi import FastAPI
import databases

DATABASE_URL = "sqlite:///mydatabase_35.db"
database = databases.Database(DATABASE_URL)
metadata2 = sqlalchemy.MetaData()


tasks = sqlalchemy.Table(
        "tasks", metadata2,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("title", sqlalchemy.String(60)),
        sqlalchemy.Column("description", sqlalchemy.String(200)),
        sqlalchemy.Column("date", sqlalchemy.String(20)),
        sqlalchemy.Column("status", sqlalchemy.String(10)),
        )
engine2 = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata2.create_all(engine2)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

# app = fastapi.FastAPI()


# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

templates = Jinja2Templates(directory='templates')


@app.post('/tasks/', response_model=None)
async def create_task(request: fastapi.Request,
                    title: str = fastapi.Form(...),
                    description: str = fastapi.Form(...),
                    date: str = fastapi.Form(...),
                    status: str = fastapi.Form(...),
                    ):
    
    new_task = insert(TaskSql).values(title=title, description=description, date=date, status=status)
    last_record_id = await database.execute(new_task)
    return {**TaskSql.model_dump(), "id": last_record_id}


@app.get("/tasks/", response_model=typing.List[pydantic_models.TaskOut])
async def read_users():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get("/tasks/{tasks_id}", response_model=pydantic_models.TaskOut)
async def read_user(user_id: int):    
    query = tasks.select().where(tasks.c.id == user_id)
    return await database.fetch_one(query)


@app.put('/tasks/{task_id}')
async def change_task(task_id: int, new_task: Task):
    
    query = select.select(TaskSql).where(TaskSql.task_id == task_id)
    task = await database.fetch_one(query)
    if not task:
        return {'updated': False}
    query = update(TaskSql).where(TaskSql.task_id == task_id).values(**new_task.model_dump())
    await database.execute(query)
    return {'updated': True, 'task': task}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):    
    query = select.select(TaskSql).where(TaskSql.task_id == task_id)
    del_task = await database.fetch_one(query)
    if not del_task:
        return {'deleted': False}
    deleted_task = delete(TaskSql).where(TaskSql.task_id == task_id)
    await database.execute(deleted_task)
    return {'deleted': True, 'deleted_task': task_id}
    