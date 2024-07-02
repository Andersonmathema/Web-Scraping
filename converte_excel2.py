import pandas as pd
import json

# Ler o arquivo Excel
file_path = 'C:\\Users\\anddr\\Downloads\\MAPAO_REYNALDODONASCIMENTOFALLEIROSDOUTOR-10236_2ªSERIEAMANHAANUAL_1 (3).xlsx'
df = pd.read_excel(file_path, sheet_name='Mapão')

# Definir o intervalo de linhas (por exemplo, da linha 16 até a linha 20, inclusive)
linha_inicio = 14  # index 15 corresponde à linha 16 (considerando 0-index)
linha_fim = 67   # index 19 corresponde à linha 20
nome_plan = '2A'

# Processar cada linha no intervalo e manter os nulos como separadores
linhas_json = []
for i in range(linha_inicio, linha_fim + 1):
    linha_desejada = df.iloc[i]
    # Ignorar a primeira coluna
    valores = linha_desejada.values[1:]
    # Substituir nulos por vírgulas
    valores_formatados = [str(v) if pd.notna(v) else "," for v in valores]
    
    # Criar a string separada por vírgulas, pulando de 4 em 4 elementos depois do nome
    nome = valores_formatados[0]
    restante = valores_formatados[1:]
    linha_str = [nome] + [",".join(restante[i:i+4]) for i in range(0, len(restante), 4)]
    
    linhas_json.append(linha_str)

# Criar um dicionário para exportar como JSON
dados = {"linhas": linhas_json}

# Exportar para um arquivo JSON
with open(f'{nome_plan}.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print(f"Dados exportados para {nome_plan}.json")

