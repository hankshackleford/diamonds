# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:41:08 2023

@author: edwar
"""

#Import packages
import pandas as pd
import pygwalker
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import streamlit as st

#Set titles and sidebar header
st.set_page_config(page_title="Diamonds", page_icon="💎", layout="wide")
st.title('Diamonds')


# Get an instance of pygwalker's renderer. You should cache this instance to effectively prevent the growth of in-process memory.
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("https://raw.githubusercontent.com/tidyverse/ggplot2/main/data-raw/diamonds.csv")
    # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
    return StreamlitRenderer(df, spec="./gw_config.json", debug=False)
 
renderer = get_pyg_renderer()
 
# Render your data exploration interface. Developers can use it to build charts by drag and drop.
renderer.render_explore()
