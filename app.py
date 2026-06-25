
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "Success", 
        "message": "Cloud-Based Web Application Deployed Successfully on AWS!"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}