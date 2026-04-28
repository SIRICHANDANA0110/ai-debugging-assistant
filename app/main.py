from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Debugging Assistant is running"
    }

@app.post("/upload-log")
async def upload_log(file: UploadFile = File(...)):
    content = await file.read()
    log_text = content.decode("utf-8", errors="ignore")

    return {
        "filename": file.filename,
        "log_preview": log_text[:1000],
        "message": "Log uploaded successfully"
    }