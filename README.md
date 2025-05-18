# Pipeline Automatizado para Dados - Temporada 2025 da Fórmula 1

<p align="center"> 
  <img src="https://github.com/user-attachments/assets/6c9c24ac-46aa-469f-9ddc-a5d4cd1946af">
</p>

Este projeto automatiza a ingestão, transformação e carga de dados da Temporada 2025 da Fórmula 1. Utilizando Airflow para orquestração, os dados são processados e armazenados em SQLite/PostgreSQL para análise.

**Tecnologias**: Python, Airflow, SQLite/PostgreSQL, Web Scraping, SQL, Git, Pandas, Streamlit

---

## Estrutura de Pastas

- **`/data`**: dados brutos e processados (CSV e scraping).
- **`/src`**: scripts Python para carga, transformação e conexão com banco de dados.
- **`/dags`**: DAGs do Airflow para orquestrar o pipeline.
- **`/sql`**: scripts SQL para criação de tabelas e consultas.
- **`/notebooks`**: notebooks para análises exploratórias.
- **`/docs`**: diagramas e prints do fluxo de dados.
- **`/f1_dashboard`**: aplicação em Streamlit para visualização dos dados.

---

## Etapas

1. **Ingestão de Dados**: Importação de dados via CSV e scraping da web (voltas rápidas).
2. **Transformação**: Limpeza, padronização e cálculo de novas colunas.
3. **Carga (ETL)**: Dados carregados em banco de dados (SQLite/PostgreSQL).
4. **Orquestração com Airflow**: Automação de tarefas via DAGs.
5. **Consultas**: Relatórios e rankings através de SQL (ex: voltas mais rápidas, desempenho de pilotos).
6. **Visualização**: Dashboard com Streamlit para insights rápidos.

---

## Como Executar

1. **Instalação**:
   ```bash
   python -m venv venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate  # Windows
   pip install -r requirements.txt

   #Rodar Carga de Dados
   python src/load_to_sqlite.py

   # Rodar Airflow
   airflow db init
   airflow webserver -p 8080
   airflow scheduler

   #Executar atualização manualmente:
   python src/load_to_sqlite.py

   #Visualizar dados com Streamlit
   streamlit run f1_app.py
