from fastapi import APIRouter, File, UploadFile
import os

router = APIRouter(prefix="/files", tags=["File Operations"])

@router.get("/list")
def list_files(directory: str = "./"):
    """
    List all files in a directory.
    """
    try:
        files = os.listdir(directory)
        return {"directory": directory, "files": files}
    except Exception as e:
        return {"error": str(e)}

@router.post("/upload")
def upload_file(file: UploadFile = File(...), destination: str = "./"):
    """
    Upload a file to the specified directory.
    """
    try:
        file_path = os.path.join(destination, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return {"message": f"File '{file.filename}' uploaded successfully to {destination}"}
    except Exception as e:
        return {"error": str(e)}
