# API de Fatos Históricos

Aplicação em Flask que mostra um fato histórico que aconteceu **no dia de hoje**, em anos anteriores.

Os dados vêm da API pública da Wikipédia em português, pelo endpoint *On this day*:

```
https://pt.wikipedia.org/api/rest_v1/feed/onthisday/events/{mes}/{dia}
```

Documentação da API da Wikipédia: https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:Central_de_pesquisas/Portal_de_dados/API

## Como funciona

1. A rota `/` pega a data atual com `datetime`.
2. Faz uma requisição GET à Wikipédia com `requests`, enviando um `User-Agent` que identifica a aplicação.
3. Pega o primeiro evento da lista e extrai o ano e o texto do fato.
4. Renderiza o template `templates/fatos.html` com a data e o fato.

## Estrutura do projeto

```
API_Flask/
├── main.py              # aplicação Flask e rota principal
├── templates/
│   └── fatos.html       # página que exibe os fatos
├── pyproject.toml       # configuração do formatador Black
├── .vscode/             # configurações do editor (opcional)
└── venv/                # ambiente virtual
```

## Requisitos

- Python 3.10 ou mais recente (o projeto foi desenvolvido com Python 3.14)
- Flask
- requests

## Como rodar

```bash
# 1. Criar o ambiente virtual (apenas na primeira vez)
python3 -m venv venv

# 2. Ativar o ambiente virtual
source venv/bin/activate

# 3. Instalar as dependências
pip install flask requests

# 4. Iniciar o servidor
python main.py
```

Depois, acesse http://127.0.0.1:5000 no navegador.

Sair do ambiente `deactivate`.

## Rotas

| Método | Rota | Descrição |
| ------ | ---- | --------- |
| GET    | `/`  | Mostra o fato histórico do dia atual |

## Formatação do código

O projeto usa o [Black](https://black.readthedocs.io/) com linhas de até 88 caracteres (configurado em `pyproject.toml`). No VS Code, a formatação acontece automaticamente ao salvar.
