# src/test_file_write.py

caminho = r"S:\F1_DataEngineer\teste.txt"

with open(caminho, "w") as f:
    f.write("Teste de escrita no arquivo\n")

print(f"Arquivo criado em: {caminho}")
