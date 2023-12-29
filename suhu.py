import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from collections import deque
import time

st.title('TEST STREAMLIT')
chart = st.empty()
data = deque(maxlen=100)
while True:
    new_data = pd.DataFrame({'time': [pd.to_datetime('now')], 'temperature': [np.random.randn()*3+25]})
    data.append(new_data)
    all_data = pd.concat(data)
    fig = px.line(all_data, x='time', y='temperature', title='Temperature Data')
    chart.plotly_chart(fig)
    time.sleep(1)
