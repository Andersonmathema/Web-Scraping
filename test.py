import pandas as pd

def lista_alunos():
    while True:
        try:
            opc = int(input("Sua escolha: "))
            if opc == 1:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/1B.csv"
            elif opc == 2:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/1C.csv"
            elif opc == 3:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/2A.csv"
            elif opc == 4:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/2B.csv"
            elif opc == 5:
                file_path = "D:/OneDrive/Projetos Python/Web Scraping/csv/2C.csv"
            else:
                print("Opção inválida. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 5.")
    
    df_excel = pd.read_csv(file_path, sep=';')
    return df_excel

# Exemplo de uso
df_alunos = lista_alunos()
print(df_alunos)