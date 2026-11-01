# Extração de tabelas de PDF para Excel

Extrai as tabelas de um PDF e salva cada uma como um arquivo Excel. O texto corrido é descartado.

## Como funciona

```text
resultado.pdf ──> LlamaParse (Markdown, uma página por arquivo) ──> regex encontra as tabelas ──> Pandas ──> .xlsx
```

1. **`main.py`** envia o PDF para o [LlamaParse](https://docs.cloud.llamaindex.ai/llamaparse/getting_started), a API de parsing da LlamaIndex, pedindo só as tabelas. Cada página volta em Markdown e é salva em `meu_pdf/paginaN.md`.
2. **`transformar_excel.py`** lê cada página, encontra os blocos de tabela Markdown com uma expressão regular, carrega cada um no Pandas (separador `|`), remove linhas e colunas vazias e grava `tabelas/PaginaNTabelaM.xlsx`.

## Como usar

Pré-requisitos: Python 3.10+ e uma chave da [LlamaCloud](https://cloud.llamaindex.ai/).

```bash
git clone https://github.com/devcauas/extracao_tabelas_excel.git
cd extracao_tabelas_excel
pip install -r requirements.txt

# a chave fica numa variável de ambiente, nunca no código
export LLAMA_CLOUD_API_KEY="sua-chave"        # Linux/macOS
# $env:LLAMA_CLOUD_API_KEY = "sua-chave"      # Windows (PowerShell)

python main.py                 # PDF -> Markdown (meu_pdf/)
python transformar_excel.py    # Markdown -> Excel (tabelas/)
```

Para outro PDF, troque `resultado.pdf` em `main.py`.

## Tecnologias

Python · LlamaParse (LlamaIndex) · Pandas · openpyxl · expressões regulares

## Limitações

- As páginas são processadas na ordem que o sistema de arquivos devolve, então a numeração dos arquivos Excel pode não seguir a ordem das páginas.
- Tabelas que o LlamaParse não reconhece como tabela Markdown ficam de fora.
