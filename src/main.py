import pandas as pd
import subprocess
import json
import config

from util.tools import get_project_root

# エクセルファイルを読み込み
df = pd.read_excel(get_project_root()+config.EXCEL_FILE_PATH, sheet_name=config.SHEET_NAME)

# GitHubにissueを作成する関数
def create_github_issue(title, body):
    url = f"https://api.github.com/repos/{config.REPO_OWNER}/{config.REPO_NAME}/issues"
    headers = {
        'Authorization': f'token {config.GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'title': title,
        'body': body
    }
    curl_command = [
        'curl', '-X', 'POST', url,
        '-H', f"Authorization: token {config.GITHUB_TOKEN}",
        '-H', 'Accept: application/vnd.github.v3+json',
        '-d', json.dumps(data)
    ]
    response = subprocess.run(curl_command, capture_output=True, text=True)
    if response.returncode == 0:
        print(f"Issue '{title}' created successfully.")
    else:
        print(f"Failed to create issue '{title}'. Response: {response.stdout}")

# データフレームからissueを読み込み、GitHubに登録
for index, row in df.iterrows():
    title = row['Title']
    body = row['Body']
    create_github_issue(title, body)
