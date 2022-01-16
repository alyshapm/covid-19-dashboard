import streamlit as st
import pandas as pd

def app():
    df = pd.read_csv("https://raw.githubusercontent.com/alyshapm/FP_AlgoProg/main/data/df_sources.csv")

    st.title('COVID-19 Dashboard')
    st.image("assets/covid.png", use_column_width=True)
    st.header("Overview")
    st.markdown("This app uses a range of COVID-19 data sources, from local and international institutions. Because I currently reside in Indonesia, this dashboard is Indonesian centric;\
                worldwide COVID-19 data visualisation, however, is also included in the app. I intend to create an interactive data visualisation on COVID-19, as well as its impact on the\
                socio-economic landscape of Indonesia.")

    st.subheader("Data & References")
    st.markdown("**I am not responsible for the quality of the data in the dataset below.**")
    st.dataframe(df)