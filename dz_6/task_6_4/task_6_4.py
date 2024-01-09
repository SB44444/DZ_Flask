from contextlib import asynccontextmanager
import databases
from fastapi import FastAPI
from sqlalchemy import create_engine, insert, update, select, delete
from sqlalchemy_models import Base, Task
from pydantic_models import TaskIn, TaskSql


DATABASE_URL = "sqlite:///mydatabase_4.sqlite"


database4 = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database4.connect()
    yield
    await database4.disconnect()

app = FastAPI(lifespan=lifespan)


@app.get('/tasks/', response_model=list[TaskSql])
async def index():
    tasks = select(Task)

    return await database4.fetch_all(tasks)


@app.get('/tasks/{task_id}/', response_model=TaskSql)
async def get_task(task_id: int):
    task = await database4.fetch_one(select(Task).where(Task.id == task_id))

    return task


@app.post('/tasks/', response_model=TaskIn)
async def add_task(task: TaskIn):
    new_task = insert(Task).values(**task.model_dump())
    await database4.execute(new_task)

    return task


@app.put('/tasks/{task_id}/', response_model=TaskSql)
async def update_task(task_id: int, task: TaskIn):
    updating_task = (update(Task).where(Task.id == task_id).values(**task.model_dump()))
    await database4.execute(updating_task)

    return await database4.fetch_one(select(Task).where(Task.id == task_id))


@app.delete('/tasks/{task_id}/')
async def delete_task(task_id: int):
    sql_query = await database4.fetch_one(select(Task).where(Task.id == task_id))
    task = TaskSql.model_validate({'id': sql_query.id, 'title': sql_query.title, 'description': sql_query.description, 'status': sql_query.status})
    deleted_task = delete(Task).where(Task.id == task_id)
    await database4.execute(deleted_task)

    return {'deleted': True, 'task': task.model_dump()}

