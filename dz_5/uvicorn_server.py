import uvicorn


if __name__ == '__main__':
    uvicorn.run('task_7:app', port=8000, reload=True)
