import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os

# Caminho absoluto local do DataWareHouse
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "db", "f1_datawarehouse.sqlite")

@st.cache_data
def load_data(table_name):
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def show_race_results():
    df = load_data("race_results")
    df_drivers = load_data("drivers")

    df.columns = df.columns.str.strip().str.lower()
    df_drivers.columns = df_drivers.columns.str.strip().str.lower()

    df = df.merge(df_drivers, how="left", left_on="driver_id", right_on="id")
    df["points"] = pd.to_numeric(df["points"], errors="coerce")
    df["position_gain"] = pd.to_numeric(df["position_gain"], errors="coerce")

    df = df.dropna(subset=["name", "points", "position_gain"])

    st.subheader("🏁 Pontuação Total por Piloto")
    pontos = df.groupby("name")["points"].sum().sort_values(ascending=False).reset_index()
    fig1 = px.bar(pontos, x="name", y="points", title="Total de Pontos por Piloto")
    st.plotly_chart(fig1)

    st.subheader("📈 Ganho Médio de Posição por Piloto")
    gain = df.groupby("name")["position_gain"].mean().sort_values(ascending=False).reset_index()
    fig2 = px.bar(gain, x="name", y="position_gain", title="Média de Ganho de Posição por Piloto")
    st.plotly_chart(fig2)    


def show_fastest_laps():
    df_fast = load_data("fastest_laps")
    df_race = load_data("race_results")
    df_drivers = load_data("drivers")

    df_fast.columns = df_fast.columns.str.strip().str.lower()
    df_race.columns = df_race.columns.str.strip().str.lower()
    df_drivers.columns = df_drivers.columns.str.strip().str.lower()

    # Evitar falhas em join
    df_fast["grand_prix"] = df_fast["grand_prix"].astype(str).str.strip().str.title()
    df_race["track"] = df_race["track"].astype(str).str.strip().str.title()

    # Manter corridas com dadosem ambas tabelas
    valid_gps = set(df_fast["grand_prix"]).intersection(set(df_race["track"]))
    df_fast = df_fast[df_fast["grand_prix"].isin(valid_gps)]

    if df_fast.empty:
        st.warning("Sem dados suficientes para exibir as voltas mais rápidas.")
        return

    # Converte tempo
    df_fast["time"] = pd.to_timedelta(df_fast["time"], errors="coerce")
    df_fast = df_fast.dropna(subset=["time"])

    # Merge com nome dos pilotos
    df_fast = df_fast.merge(df_drivers, how="left", left_on="driver_id", right_on="id")

    st.subheader("🚀 Melhor Volta por Corrida (Geral) [Somente GPs com dados completos]")
    best_laps = df_fast.loc[df_fast.groupby("grand_prix")["time"].idxmin()]
    fig3 = px.bar(best_laps, x="grand_prix", y="time", color="name", title="Melhor Volta em Cada GP")
    st.plotly_chart(fig3)

    st.subheader("🔥 Voltas Mais Rápidas por Piloto")
    count_fast = df_fast["driver_abbreviation"].value_counts().reset_index()
    count_fast.columns = ["driver_abbreviation", "voltas_mais_rapidas"]
    fig4 = px.bar(count_fast, x="driver_abbreviation", y="voltas_mais_rapidas", title="Pilotos com Mais Voltas Rápidas")
    st.plotly_chart(fig4)

def show_table_page(table_name):
    df = load_data(table_name)
    st.subheader(f"📋 Tabela - {table_name.replace('_', '').title()}")
    st.dataframe(df)
    st.subheader("📊 Estatísticas:")
    st.dataframe(df.select_dtypes(include=["number"]).describe())

def main():
    st.title("🏎️ Dashboard Fórmula 1 - Temporada 2025")
    st.sidebar.title("Escolha a Visualização")

    page = st.sidebar.radio(
        "Ir para:",
        [
            "Tabela - Resultado da Corrida",
            "Tabela - Voltas Rápidas",
            "Análises - Race_results",
            "Análises - Fast_laps"
        ]
    )

    if page == "Tabela - Resultado da Corrida":
        show_table_page("race_results")
    elif page == "Tabela - Voltas Rápidas":
        show_table_page("fastest_laps")
    elif page == "Análises - Race_results":
        show_race_results()
    elif page == "Análises - Fast_laps":
        show_fastest_laps()

if __name__ == "__main__":
    main()