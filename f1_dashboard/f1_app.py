import streamlit as st
import pandas as pd
import sqlite3  # <-- use isso no lugar de SQLAlchemy

# Caminho relativo ao banco SQLite
DB_PATH = '../db/f1_datawarehouse.sqlite'

# Carregar dados das tabelas
@st.cache_data
def load_data(table_name):
    conn = sqlite3.connect(DB_PATH)  # conexão direta
    query = f"SELECT * FROM {table_name} LIMIT 100"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def main():
    st.title("Dashboard Fórmula 1 - Temporada 2025")

    st.sidebar.title("Selecione a tabela para visualizar")
    tabela = st.sidebar.selectbox("Tabelas disponíveis", ["race_results", "fastest_laps", "drivers"])

    df = load_data(tabela)

    st.write(f"Mostrando dados da tabela: **{tabela}**")
    st.dataframe(df)

    st.write("Estatísticas descritivas:")
    st.write(df.describe(include='all'))

if __name__ == "__main__":
    main()