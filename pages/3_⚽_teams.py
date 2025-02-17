import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Teams',
)

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Selecione um clube', clubes)

df_filtered = df_data[(df_data['Club'] == club)].set_index('Name')

st.image(df_filtered.iloc[0]['Club Logo'])

st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Potential", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)","Contract Valid Until","Release Clause(£)"]

for column in columns:
    df_filtered[column] = df_filtered[column].apply(lambda x: x if isinstance(x, str) else x)

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", min_value=0, max_value=100, format="%d"
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", min_value=0, max_value=df_filtered["Wage(£)"].max(), format="£%d"),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country", width=50),
                 "Value(£)": st.column_config.ProgressColumn("Market Value", min_value=0, max_value=df_filtered["Value(£)"].max(), format="£%d"),
                 "Release Clause(£)": st.column_config.ProgressColumn("Release Clause", min_value=0, max_value=df_filtered["Release Clause(£)"].max(), format="£%d"),
             })


