# Projeto ETL com Python

Este projeto foi desenvolvido para demonstrar, de forma prática, o fluxo **ETL (Extract, Transform, Load)** usando Python e Pandas.

## Objetivo

Ler dados de usuários a partir de um arquivo CSV, gerar uma mensagem personalizada para cada registro e salvar o resultado em um novo arquivo.

## Estrutura do projeto

```text
etl-python-project/
├── data/
│   └── usuarios.csv
├── etl.py
├── requirements.txt
├── resultado.csv
├── .gitignore
└── README.md
```

## Etapas do ETL

### Extract
Leitura do arquivo `data/usuarios.csv`.

### Transform
Criação de uma coluna chamada `mensagem` com conteúdo personalizado para cada usuário.

### Load
Gravação do resultado no arquivo `resultado.csv`.

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o projeto:

```bash
python etl.py
```

## Exemplo de saída

O arquivo `resultado.csv` será gerado com a estrutura abaixo:

| nome | conta | cartao | mensagem |
|---|---:|---:|---|
| Ana Silva | 12345 | 1111 | Olá, Ana! Temos uma novidade especial para você... |

## Tecnologias utilizadas

- Python 3
- Pandas

## Autor

Projeto pronto para publicação no GitHub e entrega de atividade prática.
