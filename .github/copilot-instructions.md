## Visão rápida

Projeto pequeno com scripts Python usados para testar/checar uma API REST local e para fazer commits automáticos.

- Arquivos-chave:
  - `auto_commit_push.py` — faz append em `README.md`, comita e dá push usando GitPython; espera a variável de ambiente `GITHUB_TOKEN0` para autenticação via URL remota.
  - `crud_api_auth.py` — exemplos de testes CRUD contra o endpoint `/usuarios`; usa `BASE_URL` e `API_TOKEN` como variáveis de ambiente.
  - `health_check.py` — checagem simples da API em `http://localhost:3000/usuarios` com 3 tentativas.
  - `db.json` — dados de exemplo (usuários, produtos, pedidos) — serve como backend para `json-server` se for o caso.
  - `requirements.txt` — lista `requests` (observação: `auto_commit_push.py` importa `git.Repo` / GitPython, mas **GitPython não está** listado em `requirements.txt`).

## Objetivo para agentes de código

Se for necessário editar ou criar scripts, mantenha o estilo imperativo atual: scripts pequenos, prints informativos (com emojis), e uso de `sys.exit(1)` para falhas. Faça mudanças que sejam diretamente testáveis localmente (ex.: executar `health_check.py`, `crud_api_auth.py`).

## Como executar / exemplos (contexto do repositório)

1) Instalar dependências Python:

```bash
python3 -m pip install -r requirements.txt
# Se for usar auto_commit_push.py, instale GitPython também:
python3 -m pip install GitPython
```

2) Iniciar um backend REST local (opcional, usado por `crud_api_auth.py`):

```bash
# usando json-server (npm) com o `db.json` deste repo
npm install -g json-server
json-server --watch db.json --port 3000
```

3) Variáveis de ambiente importantes (exemplos):

```bash
export BASE_URL="http://localhost:3000/usuarios"
export API_TOKEN="token-local-teste"
# token para push no auto_commit_push.py (note o nome exato com sufixo 0)
export GITHUB_TOKEN0="ghp_xxx"
```

4) Executar os scripts:

```bash
python3 health_check.py
python3 crud_api_auth.py
python3 auto_commit_push.py
```

## Padrões e convenções observados

- Valores padrão de ambiente caem para `localhost` quando não setados (ex.: `BASE_URL` em `crud_api_auth.py`).
- Respostas HTTP são verificadas com `check_response` e o script chama `sys.exit(1)` em caso de erro — preserve esse comportamento para chamadas automatizadas.
- `auto_commit_push.py` modifica `README.md`, faz `git add`/`commit` e `push`. Ele altera a URL remota para incluir o token quando `GITHUB_TOKEN0` está presente.
- Mensagens e saídas usam JSON formatado com `json.dumps(..., ensure_ascii=False)` — preservar encoding/format quando for manipular respostas.

## Integrações e pontos de atenção

- Dependências externas: serviço REST em `BASE_URL` (por padrão `http://localhost:3000/usuarios`), Git remote (origin) acessível por URL HTTPS para push automático.
- Discrepância detectada: `auto_commit_push.py` usa `from git import Repo` (GitPython) mas `requirements.txt` não a lista. Atualize `requirements.txt` se for instalar via pip.  
- Nome da variável de token do Git é incomum: `GITHUB_TOKEN0` (com o dígito 0). Não substitua por `GITHUB_TOKEN` sem confirmação.

## Exemplos concretos (trechos relevantes)

- `auto_commit_push.py`: escreve em `README.md` e comita com a mensagem "🤖 Atualização automática via script Python"; usa `repo.remote(name="origin")` e substitui `https://` por `https://{token}@` se `GITHUB_TOKEN0` existir.
- `crud_api_auth.py`: exemplo de POST espera código 201 ao criar usuário; DELETE e PUT usam caminhos com `/usuarios/{id}`.

## O que evitar / mudanças sensíveis

- Não alterar implicitamente o nome das variáveis de ambiente usadas (p.ex. `API_TOKEN`, `BASE_URL`, `GITHUB_TOKEN0`).
- Evitar remover prints/exit behavior sem prover alternativa de sinalização se o script for usado em pipelines.

## Onde procurar ao ampliar a base de código

- Pesquise por `BASE_URL`, `API_TOKEN` e `GITHUB_TOKEN0` para localizar pontos que dependem dessas variáveis.
- `db.json` é o contrato de dados de exemplo — útil para criar mocks ou para testes locais com `json-server`.

---

Se quiser, posso ajustar o tom (mais curto ou mais detalhado), adicionar exemplos de testes automatizados mínimos ou atualizar `requirements.txt` para incluir `GitPython` e um pequeno README com passos para rodar o `json-server`.
