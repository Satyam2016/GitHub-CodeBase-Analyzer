import requests

from dotenv import load_dotenv
import os
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_PAT")

def fetch_github_repo(repo_url: str):
    """
    Fetch repository structure and metadata from GitHub.
    """
    parts = repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]
    
    api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/main?recursive=1"

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else ""
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
          contents = response.json()  # Get full JSON response
          tree = contents.get("tree", [])  # Extract 'tree' attribute
          structure = [{"name": item["path"], "type": item["type"]} for item in tree]
          return {"repository": repo, "structure": structure}
    else:
        return {"error": f"Failed to fetch repo: {response.status_code}"}

# repo_url = "https://github.com/Satyam2016/Student-Mentorship-Platform"
# repo_data = fetch_github_repo(repo_url)
# print(repo_data)
