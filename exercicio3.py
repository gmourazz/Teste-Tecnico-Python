import json

# Carregar dados do JSON
with open("faturamento.json", "r") as file:
    dados = json.load(file)

faturamento = [dia for dia in dados["faturamento"] if dia > 0]

menor_fat = min(faturamento)
maior_fat = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)

dias_acima_media = sum(1 for dia in faturamento if dia > media_mensal)

print(f"Menor faturamento: R${menor_fat:.2f}")
print(f"Maior faturamento: R${maior_fat:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
