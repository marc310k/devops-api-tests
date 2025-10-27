import os
import requests
import json
import sys

# Lê variáveis de ambiente (fallback para localhost)
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000/usuarios")
API_TOKEN = os.getenv("API_TOKEN", "token-local-teste")

def print_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))

def check_response(response, expected_code=200):
    if response.status_code != expected_code:
        print(f"❌ Erro: esperado {expected_code}, mas recebeu {response.status_code}")
        sys.exit(1)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# GET
print("➡️ [GET] Consultando usuários...")
response = requests.get(BASE_URL, headers=headers)
check_response(response)
print_json(response.json())

# POST
print("\n➡️ [POST] Criando novo usuário...")
novo_usuario = {"nome": "Carlos", "idade": 25}
response = requests.post(BASE_URL, json=novo_usuario, headers=headers)
check_response(response, 201)
print_json(response.json())

# PUT
print("\n➡️ [PUT] Atualizando usuário com ID 1...")
update_usuario = {"nome": "Marcelo Pacholak", "idade": 38}
response = requests.put(f"{BASE_URL}/1", json=update_usuario, headers=headers)
check_response(response, 200)
print_json(response.json())

# DELETE
print("\n➡️ [DELETE] Removendo usuário com ID 2...")
response = requests.delete(f"{BASE_URL}/2", headers=headers)
check_response(response, 200)
print("Status:", response.status_code)

print("\n✅ Todos os testes passaram com autenticação!")
