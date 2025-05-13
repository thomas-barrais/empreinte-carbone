import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Analyse Base E+C-", layout="wide")

# Header commun
st.markdown("""
    <style>
        .main-header {
            font-size: 36px;
            font-weight: bold;
            color: #2E8B57;
            text-align: center;
            margin-bottom: 30px;
        }
        .sub-header {
            font-size: 24px;
            font-weight: bold;
            color: #2E8B57;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>Bienvenue sur l'App qui analyse l'empreinte carbone</div>", unsafe_allow_html=True)

# Navigation entre les pages
page = st.sidebar.radio("Navigation", ["Analyse", "Contact"])

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Read Excel file into DataFrame
    df = pd.read_excel(uploaded_file)

    # Display DataFrame
    st.subheader("Excel File Contents")
    st.write(df)