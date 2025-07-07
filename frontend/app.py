import streamlit as st
import requests

st.title("📈  Earnings Call Analyzer")

call_text = st.text_area("Paste earnings call transcript here:", height=300)

if st.button("Analyze"):
    res = requests.post("http://localhost:8000/analyze/", data={"text": call_text})
    output = res.json()

    st.subheader("📝  Summary")
    st.write(output["summary"])

    st.subheader("📊  Sentiment")
    st.write(output["sentiment"])

    st.subheader("💡  Key Insights")
    st.write(output["insights"])
