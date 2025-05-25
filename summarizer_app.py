import streamlit as st
from personalized_news import text_summarizer_after_ft

st.set_page_config(page_title="Newton News Summarizer", layout="wide")
st.title("\U0001F4F0 NEWTON: Tons of News Summarized")

with st.expander("⚙️ Customize Summary Settings", expanded=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        max_length = st.slider("Max Summary Length", min_value=50, max_value=512, value=160, step=10)
        min_length = st.slider("Min Summary Length", min_value=10, max_value=200, value=60, step=10)
    
    with col2:
        num_beams = st.selectbox("Number of Beams (Quality vs. Speed)", [1, 2, 4, 5, 8], index=3)
        length_penalty = st.slider("Length Penalty", min_value=0.1, max_value=4.0, value=2.5, step=0.1)

    with col3:
        ngram_blocking = st.checkbox("Avoid repeated phrases (no_repeat_ngram)", value=True)
        no_repeat_ngram_size = 3 if ngram_blocking else 0

st.markdown("---")
article = st.text_area("📰 Paste multiple related news articles here:", height=400)

if st.button("📄 Summarize"):
    if article.strip() == "":
        st.warning("Please paste some content before summarizing.")
    else:
        with st.spinner("Generating summary..."):
            summary = text_summarizer_after_ft(
                article,
                max_length=max_length,
                min_length=min_length,
                num_beams=num_beams,
                length_penalty=length_penalty,
                no_repeat_ngram_size=no_repeat_ngram_size
            )
        st.subheader("📝 Summary:")
        st.write(summary)
st.markdown("""
    <style>
        .pill-button {
            display: inline-block;
            padding: 10px 25px;
            border-radius: 999px;
            background-color: #4CAF50;
            color: white !important;
            text-decoration: none !important;
            font-weight: 600;
            font-size: 16px;
            border: none;
            cursor: pointer;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
            transition: all 0.2s ease-in-out;
        }
        .pill-button:hover {
            background-color: #3e9141;
            box-shadow: 0px 6px 8px rgba(0,0,0,0.15);
        }
    </style>

    <a href="https://newton-news-dashboard.streamlit.app/" target="_blank" class="pill-button">📊 View ROUGE Scores Dashboard</a>
""", unsafe_allow_html=True)
