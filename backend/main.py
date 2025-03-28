from fastapi import FastAPI
from fastapi.responses import FileResponse
from .github_fetch import fetch_github_repo

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "GitHub Analyzer API"}

@app.get("/repoDetail")
def repo_detail(url: str):
    return fetch_github_repo(url)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")  # Serves the favicon
