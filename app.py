import streamlit as st
from scraper import scrape_laptops
from cleaning import clean_data
from eda import perform_eda
import pandas as pd
import os

st.title("""💻 Laptop Price Scraper &  Analyzer""")

# Scrape Button
if st.button("Scrape Data"):
    st.write("🔍 Scraping latest laptop data...")
    df = scrape_laptops()
    if df.empty:
        st.error("❌ Failed to scrape data.")
    else:
        st.success("✅ Data scraped and saved to laptops_raw.csv")

# Clean Button
if st.button("Clean Data"):
    if os.path.exists("laptops_raw.csv"):
        df = clean_data()
        st.success("✅ Data cleaned!")
        st.write(df.head())
    else:
        st.warning("⚠️ No raw data found. Please scrape first.")

# EDA Button
if st.button("Show Price Distribution"):
    if os.path.exists("laptops_cleaned.csv"):
        perform_eda()
        st.image("price_distribution.png", caption="Price Distribution", use_column_width=True)
    else:
        st.warning("⚠️ No cleaned data available.")
