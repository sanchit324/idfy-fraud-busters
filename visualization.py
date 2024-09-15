import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_pii_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(y='PII_Detected', data=df, order=df['PII_Detected'].explode().value_counts().index)
    plt.title('PII Distribution')
    st.pyplot(plt)

def plot_risk_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Risk_Score'], bins=30, kde=True)
    plt.title('Risk Score Distribution')
    st.pyplot(plt)

def plot_pii_risk(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Sensitivity_Score', y='Risk_Score', data=df)
    plt.title('Sensitivity Score vs Risk Score')
    st.pyplot(plt)
