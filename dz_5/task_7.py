"""Задание 
Необходимо создать API для управления списком задач.
Каждая задача должна содержать заголовок и описание.
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
API должен содержать следующие конечные точки:
○ GET /tasks - возвращает список всех задач.
○ GET /tasks/{id} - возвращает задачу с указанным идентификатором.
○ POST /tasks - добавляет новую задачу.
○ PUT /tasks/{id} - обновляет задачу с указанным идентификатором.
○ DELETE /tasks/{id} - удаляет задачу с указанным идентификатором.
Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.
"""

from datetime import datetime
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic_models import Task

app = FastAPI()
templates = Jinja2Templates(directory='templates')
tasks: list[Task] = []


@app.get('/')
@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('tasks.html', {'request': request, 'tasks': tasks})


@app.get("/tasks/{item_id}", response_model=Task)
async def get_item_by_id(item_id: int):
    task = [task for task in tasks if task.id == item_id]
    if task:
        return task[0]
    raise HTTPException(status_code=404, detail="Задача с указанным id не найдена")


@app.post('/tasks')
@app.post('/tasks/')
def add_task(
        request: Request, title: str = Form(...), description: str = Form(...), status: bool = Form(False),
        date_: datetime = Form(...),
        task_id: int = Form(...),):
    task = Task(task_id=task_id, title=title, description=description, date_=date_, status=status)
    tasks.append(task)
    return templates.TemplateResponse('tasks.html', {'request': request, 'tasks': tasks})


@app.put('/tasks/{task_id}')
def change_task(task_id: int, new_task: Task):
    filtered_task = [task for task in tasks if task.task_id == task_id]
    if not filtered_task:
        return {'updated': False}
    task = filtered_task[0]
    task.title = new_task.title
    task.description = new_task.description
    task.status = new_task.status
    return {'updated': True, 'task': task}


@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    del_tasks = [task for task in tasks if task.task_id == task_id]
    if not del_tasks:
        return {'deleted': False}

    tasks.remove(del_tasks[0])
    return {'deleted': True, 'task': del_tasks[0]}
