import pandas as pd

data = 'C:\\Users\\anddr\\Downloads\\planilha_modificada.xlsx'
path_xport = 'C:/Users/anddr/Downloads/planilha_formatada.xlsx'
path_json = 'C:/Users/anddr/Downloads/planilha_formatada.json'

def limpa_organiza():   
    planilha = pd.read_excel(data, header=[0, 2], skiprows=12)
    planilha.drop(index=1, inplace=True)
    planilha.dropna(axis=1, how='all', inplace=True)
    planilha.dropna(axis=0, how='all', inplace=True)
    planilha = planilha.loc[:, planilha.columns.get_level_values(1) != 'Nº']
    planilha = planilha.sort_values(by=[('Aluno', 'Nome'), ('Aluno', 'Sit')])
    
    
    # # Converter colunas numéricas para o tipo float ou int
    # for col in planilha.columns:
    #     try:
    #         planilha[col] = pd.to_numeric(planilha[col], errors='coerce')
    #     except Exception as e:
    #         print(f"Não foi possível converter a coluna {col}: {e}")

    return planilha

def exporta_excel():
    planilha = limpa_organiza()
    planilha.to_excel(path_xport, index=True)
    print("Planilha exportada com sucesso!")

def exporta_json():
    planilha = limpa_organiza()
    planilha.to_json(path_json, orient='records', lines=True)
    print("Planilha exportada em formato JSON com sucesso!")

if __name__ == '__main__':
    limpa_organiza()
    exporta_excel()
    exporta_json()


