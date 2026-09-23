import streamlit as st

from config.settings import APP_NAME, APP_TAGLINE


st.set_page_config(
    page_title=APP_NAME,
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title(APP_NAME)
st.caption(APP_TAGLINE)

st.success("AgreeWise foundation is running successfully.")

st.write(
    "Phase 1 health check: Streamlit application initialized."
)
