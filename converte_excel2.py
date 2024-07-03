import pandas as pd
import json

# Ler o arquivo Excel
file_path = 'C:\\Users\\anddr\\Downloads\\MAPAO_REYNALDODONASCIMENTOFALLEIROSDOUTOR-10236_2ªSERIEAMANHAANUAL_1 (3).xlsx'
df = pd.read_excel(file_path, sheet_name='Mapão')

# Definir o intervalo de linhas (por exemplo, da linha 16 até a linha 20, inclusive)
linha_inicio = 14  # index 15 corresponde à linha 16 (considerando 0-index)
linha_fim = 66   # index 67 corresponde à linha 68
nome_plan = '2A'

# Metadados
metadados = ["Nome", "Língua Portuguesa", "Educação Física", "Geografia", "História", "Sociologia", "Biologia", "Física", "Matemática", "Química", "Projeto de Vida", "Educação Financeira", "Redação e Leitura", "Inglês", "Total"]

# Processar cada linha no intervalo e manter os nulos como separadores
linhas_json = []
for i in range(linha_inicio, linha_fim + 1):
    linha_desejada = df.iloc[i]
    # Ignorar a primeira coluna
    valores = linha_desejada.values[1:-1]
    # Substituir nulos por vírgulas
    valores_formatados = [str(v) if pd.notna(v) else "," for v in valores]
    
    # Criar a string separada por vírgulas, pulando de 4 em 4 elementos depois do nome
    nome = valores_formatados[0]
    restante = valores_formatados[5:]
    
    linha_str = [nome] + [",".join(restante[i+1:i+4]) for i in range(0, len(restante), 5)]
    
    linhas_json.append(linha_str)

# Adicionar metadados ao JSON
dados = {"metadados": metadados, "linhas": linhas_json}

# Exportar para um arquivo JSON
with open(f'{nome_plan}.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print(f"Dados exportados para {nome_plan}.json")


