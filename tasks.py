from celery import Celery

app = Celery('tasks', broker="redis://localhost/1", backend="redis://localhost/1")

@app.task
def add(x, y):
    return x + y

@app.task
def div():
    return 7 / 0
