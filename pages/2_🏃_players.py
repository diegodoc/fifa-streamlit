import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Players',
    page_icon=':soccer:',
    )

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Selecione um clube', clubes)

df_players = df_data[df_data['Club'] == club]

players = df_players = df_data[df_data['Club'] == club]['Name'].unique()
player = st.sidebar.selectbox('Selecione um jogador', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

st.markdown(f"**Club:** {player_stats['Club']}")
st.markdown(f"**Position:** {player_stats['Position']}")
st.markdown(f"**Nationality:** {player_stats['Nationality']}")
st.markdown(f"**Age:** {player_stats['Age']}")

st.divider()

st.subheader(f"**Overall Rating:** {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)

col1.metric(label='Market Value', value=f'£{player_stats["Value(£)"]:,}')
col2.metric(label='Wage', value=f'£{player_stats["Wage(£)"]:,}')
col3.metric(label='Release Clause', value=f'£{player_stats['Release Clause(£)']:,}')








