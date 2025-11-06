from fastapi import FastAPI

app = FastAPI(
    title="Tickt",
    version="0.1",
    description="Backend service for Todo List project (Sprint 1)."
)

# Временное хранилище задач
todos = []

@app.get("/")
def root():
    return {"message": "Welcome to Tickt"}

@app.get("/todos")
def get_todos():
    return {"todos": todos}

@app.post("/todos")
def add_todo(item: dict):
    todos.append(item)
    return {"message": "Todo added", "item": item}
