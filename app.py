import os
import streamlit as st
from lib.db import neo4j, example_match_persons

def home():
    persons = example_match_persons()
    for person in persons:
        st.write(f"- {person}")
    

if __name__ == "__main__":
    st.set_page_config(
        page_title="MyApp",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state = "collapsed"
    )
    views = {
        "Home": home,
    }
    selected_views = st.sidebar.selectbox(label="Page", options=views.keys())
    render_view = views[selected_views]
    render_view()