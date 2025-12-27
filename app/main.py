from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MiniSupport API skeleton is running"}
