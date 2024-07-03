import pandas as pd
import json

nome = "2A"
# Caminho para o arquivo JSON
json_file_path = '2A.json'

# Ler o arquivo JSON
with open(json_file_path, 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Extrair metadados e linhas
metadados = dados['metadados']
linhas = dados['linhas']

# Preparar listas de dicionários para converter em DataFrames
dados_formatados_disciplinas = []
dados_formatados_totais = []

# Conjunto para acompanhar alunos únicos
alunos_unicos = set()

for linha in linhas:
    aluno = linha[0]
    for i, meta in enumerate(metadados[1:-1], start=1):  # Ignorar a última coluna que é "Total"
        notas_faltas_aulas = linha[i].split(',')
        dados_formatados_disciplinas.append({
            "Aluno": aluno,
            "Disciplina": meta,
            "Nota": float(notas_faltas_aulas[0]) if notas_faltas_aulas[0] != '-' else 0,
            "Faltas": float(notas_faltas_aulas[1]) if notas_faltas_aulas[1] != '-' else 0,
            "Ausências": float(notas_faltas_aulas[2]) if notas_faltas_aulas[2] != '-' else 0
        })
    # Adicionar as colunas separadas do "Total" se o aluno ainda não foi adicionado
    if aluno not in alunos_unicos:
        total_valores = linha[-1].split(',')  # Última coluna é "Total"
        dados_formatados_totais.append({
            "Aluno": aluno,
            "Percentual Bimestre": float(total_valores[0]) if total_valores[0] != '-' else 0,
            "Faltas Anuais": float(total_valores[1]) if total_valores[1] != '-' else 0,
            "Frequência Anual": float(total_valores[2]) if total_valores[2] != '-' else 0
        })
        alunos_unicos.add(aluno)

# Converter as listas de dicionários em DataFrames
df_disciplinas = pd.DataFrame(dados_formatados_disciplinas)
df_totais = pd.DataFrame(dados_formatados_totais)

# Substituir valores nulos por zeros e ajustar os tipos de dados
df_disciplinas = df_disciplinas.fillna(0).infer_objects(copy=False)
df_totais = df_totais.fillna(0).infer_objects(copy=False)

# Ordenar por nome de aluno e disciplina em ordem alfabética
df_disciplinas = df_disciplinas.sort_values(by=["Aluno", "Disciplina"])
df_totais = df_totais.sort_values(by=["Aluno"])

# Exportar para um arquivo Excel com duas planilhas
excel_file_path = f'{nome}.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    df_disciplinas.to_excel(writer, index=False, sheet_name='Disciplinas')
    df_totais.to_excel(writer, index=False, sheet_name='Totais Anuais')

print(f"Dados exportados para {excel_file_path}")







    
    
    
    

