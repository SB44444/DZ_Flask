import uvicorn


if __name__ == '__main__':
    uvicorn.run('task_35:app', port=8000, reload=True)
