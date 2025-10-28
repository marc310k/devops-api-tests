import os
from git import Repo
from datetime import datetime

# Direotorio atual do projeto
LOCAL_DIR = os.getcwd()
TARGET_FILE = "README.md"
BRANCH_NAME = "main"

print(f"📂 Diretório do repositório: {LOCAL_DIR}")

# Abre o repositorio existente 
repo = Repo(LOCAL_DIR)

# Edita o arquivo
file_path = os.path.join(LOCAL_DIR, TARGET_FILE)
with open(file_path, "a") as f:
    f.write(f"\nAtualização automática em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Commit
repo.git.add(TARGET_FILE)
repo.index.commit("🤖 Atualização automática via script Python")  

# Push
print("🚀 Enviando commit...")
origin = repo.remote(name="origin")
token = os.getenv("GITHUB_TOKEN")

if token:
    username = "marc310k"
    remote_url = f"https://{username}:{token}@github.com/marc310k/devops-api-tests.git"
    origin.set_url(remote_url)

origin.push()


origin.push()
print("✅ Push concluido!")