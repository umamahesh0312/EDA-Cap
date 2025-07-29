# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def perform_eda(cleaned_file='laptops_cleaned.csv', raw_file='laptops_raw.csv'):
    st.subheader("Exploratory Data Analysis 📊")

    # File download buttons
    st.sidebar.subheader("📁 Download Files")
    try:
        with open(raw_file, 'rb') as f:
            st.sidebar.download_button("Download Raw CSV", f, file_name=raw_file, mime='text/csv')
    except FileNotFoundError:
        st.sidebar.warning("Raw CSV file not found.")

    try:
        with open(cleaned_file, 'rb') as f:
            st.sidebar.download_button("Download Cleaned CSV", f, file_name=cleaned_file, mime='text/csv')
    except FileNotFoundError:
        st.sidebar.warning("Cleaned CSV file not found.")

    # Load cleaned data
    try:
        df = pd.read_csv(cleaned_file)
    except FileNotFoundError:
        st.error("❌ Cleaned data file not found.")
        return

    st.write("### 🧾 Sample Data")
    st.dataframe(df.head())

    # Ensure price column exists and is numeric
    if 'price' not in df.columns or df['price'].isnull().all():
        st.warning("⚠️ No valid 'price' data found.")
        return

    if df['price'].dtype not in ['int64', 'float64']:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')

    df = df.dropna(subset=['price'])

    # Plot price distribution
    st.write("### 💰 Price Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['price'], kde=True, ax=ax)
    ax.set_title("Laptop Price Distribution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Frequency")
    st.pyplot(fig, use_container_width=True)
