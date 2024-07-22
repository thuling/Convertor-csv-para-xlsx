import pandas as pd
import os

def csv_to_excel(csv_folder_path):
    for filename in os.listdir(csv_folder_path):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(csv_folder_path, filename)
            excel_file_path = os.path.join(csv_folder_path, filename.replace('.csv', '.xlsx'))
            
            try:
                df = pd.read_csv(csv_file_path, encoding='utf-8', sep=';', on_bad_lines='skip')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
                except Exception as e:
                    print(f"Não foi possível ler o arquivo {csv_file_path}: {e}")
                    continue
            
            df.to_excel(excel_file_path, index=False)
            print(f"Convertido {filename} para {excel_file_path}")

csv_folder_path = ''  # Substitua pelo caminho do diretório dos seus arquivos CSV

csv_to_excel(csv_folder_path)
