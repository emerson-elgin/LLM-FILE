from fastapi import FastAPI
from backend.app.routes import file_operations

app = FastAPI(
    title="LLM-Based File Management System",
    description="A system for efficient file management with AI capabilities.",
    version="0.1.0"
)

# Include routes
app.include_router(file_operations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the File Management System API"}
