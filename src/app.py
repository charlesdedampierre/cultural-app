from graph import make_figure
import streamlit as st
import pandas as pd


df_decade = pd.read_csv("src/data/df_region_decade.csv", index_col=[0])
list_countries = sorted(list(set(df_decade.meta_country)))

st.set_page_config(
    layout="wide",
    page_icon=":)",
    initial_sidebar_state="collapsed",
    page_title="Cultural 2.0",
)

st.title("Cultura 2.0")

col1, col2 = st.columns([1, 4])

with col1:
    min_time_select = st.number_input(label="Min Date", value=1000, step=50)
    max_time_select = st.number_input(label="Max Date", value=1600, step=50)
    country_select = st.selectbox(
        label="Chose the country", options=list_countries, index=0,
    )

with col2:
    fig = make_figure(
        min_time=min_time_select,
        max_time=max_time_select,
        meta_country=country_select,
        width=1200,
        height=700,
        top_individuals=10,
    )
    st.plotly_chart(fig)
    # fig.show()
