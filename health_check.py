import requests
import sys
import time

API_URL = "http://localhost:3000/usuarios"

def check_api(url):
    try:
        print(f"🔍 Verificando {url}...")
        r = requests.get(url, timeout=3)

        if r.status_code == 200:
            print("✅ API está online e respondendo corretamente!")
            return True
        else:
            print(f"⚠️ API respondeu com código: {r.status_code}")
            return False
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao conectar: {e}")
        return False
    
# tenta 3 vezes antes de falhar 
for attempt in range(1, 4):
    if check_api(API_URL):
        sys.exit(0)
    else:
        print(f"⏳ Tentativa {attempt}/3 falhou. Tentando novamente...")
        time.sleep(2)

print("❌ API não respondeu após 3 tentativas.")
sys.exit(1)      