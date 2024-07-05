import pandas as pd

data  = 'C:\\Users\\anddr\\Downloads\\MAPAO_REYNALDODONASCIMENTOFALLEIROSDOUTOR-10236_2ªSERIEAMANHAANUAL_1.xlsx'
planilha = pd.read_excel(data,skiprows=10 )

def cabecalho():
    lista_disciplinas = [planilha.loc[0].dropna()]    
    planilha.columns = lista_disciplinas[:len(planilha.columns)] 


if __name__ == '__main__':    
    
    planilha = pd.read_excel(data,skiprows=14 )
    #cabecalho()
    planilha.dropna(axis=1, how='all', inplace=True)
    #planilha.drop()
    print(planilha)

# output_excel = 'C:\\Users\\anddr\\Downloads\\planilha_modificada.xlsx'
# planilha.to_excel(output_excel, index=False)
