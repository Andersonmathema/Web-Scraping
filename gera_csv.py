import pandas as pd
from unidecode import unidecode

# Função para gerar o ID no formato desejado
def gerar_id(nome, ra, digito):
    nome_sem_acento = unidecode(nome)
    parte_nome = nome_sem_acento.replace(" ", "")[:11].lower()
    parte_ra = str(ra[1:])
    id_aluno = f"{parte_nome}{parte_ra}{digito}-sp"
    return id_aluno

# Carregar o arquivo Excel
file_path = "D:\\OneDrive\\Projetos Python\\Web Scraping\\1C.xlsx"
df_excel = pd.read_excel(file_path)

# Supõe que os nomes estão na coluna 'Nome', o RA na coluna 'RA', e o dígito na coluna 'Digito'
# Ajuste os nomes das colunas conforme necessário
dados = df_excel[['No','Nome', 'RA', 'Digito']].values.tolist()

# Gerar a lista de IDs
lista_ids = []
for no, nome, ra, digito in dados:
    id_aluno = gerar_id(nome, str(ra), str(digito))
    lista_ids.append((no, nome, id_aluno))

# Criar um DataFrame
df = pd.DataFrame(lista_ids, columns=["No", "Nome", "ID_Aluno"])

# Salvar o DataFrame em um arquivo CSV separado por ponto e vírgula
csv_file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/1C.csv"
df.to_csv(csv_file_path, sep=';', index=False)

print(f"Arquivo CSV salvo em: {csv_file_path}")



