import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv('./datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    st.session_state['data'] = df_data
    
st.markdown('# FIFA23 OFFICIAL DATASET!')
st.markdown(' The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. With over 17,000 records, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.')
btn = st.button("Acesse os dados do Kaggle!")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

df_data
st.sidebar.markdown('Desenvolvido por Diego Clemente')

