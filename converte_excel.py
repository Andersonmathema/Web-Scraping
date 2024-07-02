import pandas as pd

# Ler o arquivo Excel
file_path = 'C:\\Users\\anddr\\Downloads\\MAPAO_REYNALDODONASCIMENTOFALLEIROSDOUTOR-10236_2ªSERIEAMANHAANUAL_1 (3).xlsx'
df = pd.read_excel(file_path, sheet_name='Mapão')

# Definir o intervalo de linhas (por exemplo, da linha 16 até a linha 20, inclusive)
nome = '2A'
linha_inicio = 14  # considerando 0-index
linha_fim = 67    

# Processar cada linha no intervalo
linhas_txt = []
for i in range(linha_inicio, linha_fim + 1):
    linha_desejada = df.iloc[i]
    valores_filtrados = linha_desejada.dropna()
    linha_txt = ' '.join(map(str, valores_filtrados.values))
    linhas_txt.append(linha_txt)

# Exportar todas as linhas processadas para um arquivo de texto
with open(f'{nome}.txt', 'w') as f:
    for linha in linhas_txt:
        f.write(linha + '\n')

print("Dados exportados para saida.txt")

