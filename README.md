# Pipeline Automatizado para Dados - Temporada 2025 da Fórmula 1

<p align="center"> 
  <img src="https://github.com/user-attachments/assets/6c9c24ac-46aa-469f-9ddc-a5d4cd1946af">
</p>

Este projeto automatiza a ingestão, transformação e carga de dados da Temporada 2025 da Fórmula 1. Utilizando Airflow para orquestração, os dados são processados com armazenamento local em SQLite (podendo ser migrado para PostgreSQL).

📊 Um dashboard interativo com **Streamlit + Plotly** apresenta insights visuais dos resultados das corridas e voltas mais rápidas.

---

## 🚀 Tecnologias e Ferramentas

- **Python** (pandas, requests, BeautifulSoup)
- **Airflow** (via Docker)
- **SQLite** (ou PostgreSQL opcional)
- **Streamlit** (visualização de dados)
- **Papermill** (execução automática de notebooks)
- **Plotly** (gráficos interativos)
- **Git/GitHub** (controle de versão)

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
  # Linux/Mac
  source .venv/bin/activate

  # Windows
  .venv\Scripts\activate

  # Instalar dependências
  pip install -r requirements.txt


  #(Manualmente) Coletar dados das corridas e voltas mais rápidas
  python src/ingest_race_results.py
  python src/scrape_fastest_laps.py

  # Executar consultas SQL manualmente:Carregar no banco de dados SQLite + executar queries
  python src/load_and_query_sqlite.py

  #  Utilizando o Apache Airflow com Docker + Docker Compose
   
  # Subir os containers do Airflow 
  docker compose -f docker/airflow/docker-compose.yaml up -d

  # Parar os containers 
  docker compose -f docker/airflow/docker-compose.yaml down

  #Visualizar dados com Streamlit
  python -m streamlit run f1_dashboard/f1_app.py
