import pandas as pd

data  = 'C:\\Users\\anddr\\Downloads\\MAPAO_REYNALDODONASCIMENTOFALLEIROSDOUTOR-10236_2ªSERIEAMANHAANUAL_1.xlsx'
planilha = pd.read_excel(data,skiprows=14 )
#planilha = planilha.loc[:, ~planilha.columns.str.contains('^Unnamed')]
planilha.dropna(axis=1, how='all', inplace=True)
for plan in planilha.columns:
    planilha.drop(planilha.columns[range(0,len(planilha),5)])
print(planilha)
# print(planilha[13:len(planilha)-1])
#print(planilha.loc[13:len(planilha)-1].dropna)
output_excel = 'C:\\Users\\anddr\\Downloads\\planilha_modificada.xlsx'
planilha.to_excel(output_excel, index=False)