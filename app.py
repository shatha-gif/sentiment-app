import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Sentiment Visualization (Pie + Bar)")

# --------------------------
# Upload CSV
# --------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Preview of Data")
    st.write(df.head())

    # --------------------------
    # Select Sentiment Column
    # --------------------------
    column = st.selectbox("Select the sentiment column", df.columns)

    # Normalize sentiment text
    df[column] = df[column].astype(str).str.strip().str.lower()

    # Count sentiments
    sentiment_counts = {
        "Positive": (df[column] == "positive").sum(),
        "Neutral": (df[column] == "neutral").sum(),
        "Negative": (df[column] == "negative").sum()
    }

    st.write("### Sentiment Counts")
    st.write(sentiment_counts)

    # --------------------------
    # PIE CHART
    # --------------------------
    st.write("## 🥧 Pie Chart")
    fig1, ax1 = plt.subplots()
    ax1.pie(
        sentiment_counts.values(),
        labels=sentiment_counts.keys(),
        autopct="%1.1f%%"
    )
    ax1.axis("equal")
    st.pyplot(fig1)

    # --------------------------
    # BAR CHART
    # --------------------------
    st.write("## 📊 Bar Chart")
    fig2, ax2 = plt.subplots()
    ax2.bar(sentiment_counts.keys(), sentiment_counts.values())
    ax2.set_ylabel("Count")
    ax2.set_title("Sentiment Distribution")
    st.pyplot(fig2)
