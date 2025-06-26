from agents.classificador import classificar_documento

# Altere esse nome para o documento que quer testar
NOME_ARQUIVO = "docs/contrato_amostra.txt"

with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
    texto = f.read()

resultado = classificar_documento(texto)

print("🧠 Tipo detectado:", resultado["tipo_documento"])
print("📂 Subtipo:", resultado["subtipo"])
print("📊 Confiança:", resultado["confiança"])
print("🧾 Racional:", resultado["racional"])
