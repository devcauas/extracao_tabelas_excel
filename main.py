import os

# A chave da LlamaCloud vem da variável de ambiente LLAMA_CLOUD_API_KEY (ver README)
if not os.getenv("LLAMA_CLOUD_API_KEY"):
    raise SystemExit("Defina a variável de ambiente LLAMA_CLOUD_API_KEY antes de rodar.")

from llama_parse import LlamaParse

documentos = LlamaParse(result_type="markdown", system_prompt="this file contains text and tables, I'd like to get only the tables from the text").load_data("resultado.pdf")

print(len(documentos))

for i, pagina in enumerate(documentos):
    with open(f"meu_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)
