import pandas as pd

# Carregar o arquivo .xls (ou .html) para um DataFrame
data = 'C:\\Users\\anddr\\Downloads\\MAPAO_REYNALDODONASCIMENTOFALLEIROSDOUTOR-10236_2ªSERIEAMANHAANUAL_1.xls'  # Ajuste o caminho do arquivo conforme necessário
planilha = pd.read_html(data)[0]

# Habilitar a edição (modificações podem ser feitas diretamente no DataFrame)
planilha.drop(columns=[0,1,2], inplace=True)

print(planilha.head(10))


# Salvar a planilha como .xlsx
output_excel = 'C:/Users/anddr/Downloads/planilha_modificada.xlsx'
planilha.to_excel(output_excel, index=False, engine='openpyxl')

print(f"Planilha salva como {output_excel}")
