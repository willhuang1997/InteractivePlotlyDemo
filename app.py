# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import streamlit as st

import requests
import base64

st.set_page_config(
    page_title="Interactive Plotly Demo",
    page_icon="📈",
    layout="wide",
)

# Function to download file and convert it to a downloadable format
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}">{file_label}</a>'
    return href

# URL of the file to be downloaded
file_url = "https://github.com/willhuang1997/InteractivePlotlyDemo/raw/main/streamlit-1.27.2-py2.py3-none-any.whl"

# Create Streamlit layout
st.title("Interactive Plotly Streamlit Wheel File")
st.write("Click the link below to download the wheel file:")

# Fetching the file from the URL
response = requests.get(file_url)
filename = file_url.split("/")[-1]

# Saving the file fetched from the URL
with open(filename, "wb") as file:
    file.write(response.content)

# Creating the download link
st.markdown(get_binary_file_downloader_html(filename, 'Click here to download'), unsafe_allow_html=True)

st.header("Tip 1: when selecting or zooming / panning, Double click to reset")
st.header("Tip 2: When selecting (lasso or box), shift to do another selection and not get rid of ur current selection!")

# BUBBLE CHART
df_bubble = px.data.gapminder()
fig_bubble = px.scatter(
    df_bubble.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

# UI: Checkboxes to select events
st.header("Event Selectors for a Bubble chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

# Sample Data
df_bubble = px.data.gapminder()
fig_bubble = px.scatter(
    df_bubble.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Bubble")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Bubble")
on_hover = st.checkbox("On Hover", key="oh_Bubble")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Bubble")

with st.expander("Original Data:"):
    st.write(df_bubble.query("year==2007"))

return_value = st.plotly_chart_widget(
    fig_bubble,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="bubble_chart",
)

# Optionally display return values
st.dataframe(return_value)
    """)
on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Bubble")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Bubble")
on_hover = st.checkbox("On Hover", key="oh_Bubble")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Bubble")

with st.expander("Original Data:"):
    st.write(df_bubble.query("year==2007"))

return_value = st.plotly_chart_widget(
    fig_bubble,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="bubble_chart",
)

# Optionally display return values
st.dataframe(return_value)

# CANDLESTICK CHART
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig_candlestick = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

# UI: Checkboxes to select events
st.header("Event Selectors for a Candlestick chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig_candlestick = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Candlestick")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Candlestick")
on_hover = st.checkbox("On Hover", key="oh_Candlestick")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Candlestick")

with st.expander("Original Data:"):
    st.write(df)

return_value = st.plotly_chart_widget(
    fig_candlestick,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="candlestick_chart",
)

# Optionally display return values
st.dataframe(return_value)
    """)
on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Candlestick")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Candlestick")
on_hover = st.checkbox("On Hover", key="oh_Candlestick")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Candlestick")

with st.expander("Original Data:"):
    st.write(df)

return_value = st.plotly_chart_widget(
    fig_candlestick,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="candlestick_chart",
)

# Optionally display return values
st.dataframe(return_value)

# BAR CHART
data_canada = px.data.gapminder().query("country == 'Canada'")
fig_bar = px.bar(data_canada, x='year', y='pop')

# UI: Checkboxes to select events
st.header("Event Selectors for a Bar chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

# BAR CHART
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')

st.write("Original Data:")
st.write(data_canada)

on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Bar")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Bar")
on_hover = st.checkbox("On Hover", key="oh_Bar")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Bar")

with st.expander("Original Data:"):
    st.write(data_canada)

return_value = st.plotly_chart_widget(
    fig_bar,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="bar_chart",
)

# Optionally display return values
st.dataframe(return_value)
    """)
on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Bar")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Bar")
on_hover = st.checkbox("On Hover", key="oh_Bar")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Bar")

with st.expander("Original Data:"):
    st.write(data_canada)

# Assuming `st.plotly_chart_widget` is available in your environment. Otherwise, replace with `st.plotly_chart`.
return_value = st.plotly_chart_widget(
    fig_bar,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="bar_chart",
)

# Optionally display return values
st.dataframe(return_value)

# Generate some data
df = px.data.iris() # iris is a pandas DataFrame
fig_scatter = px.scatter(df, x="sepal_width", y="sepal_length")

# UI: Checkboxes to select events
st.header("Event Selectors for a Scatter Plot")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

# Generate some data
df = px.data.iris() # iris is a pandas DataFrame
fig_scatter = px.scatter(df, x="sepal_width", y="sepal_length")

# UI: Checkboxes to select events
st.header("Event Selectors for a Scatter Plot")

on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Scatter")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Scatter")
on_hover = st.checkbox("On Hover", key="oh_Scatter")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Scatter")

with st.expander("Original Data:"):
    st.write(df)

return_value = st.plotly_chart_widget(
    fig_scatter,
    use_container_width=True,
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="scatter_chart",
)

# Optionally display return values
st.dataframe(return_value)
    """)

on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Scatter")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Scatter")
on_hover = st.checkbox("On Hover", key="oh_Scatter")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Scatter")

with st.expander("Original Data:"):
    st.write(df)

return_value = st.plotly_chart_widget(
    fig_scatter,
    use_container_width=True,
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="scatter_chart",
)

# Optionally display return values
st.dataframe(return_value)

# HISTOGRAM CHART
df = px.data.tips()
fig_histogram = px.histogram(df, x="day", category_orders=dict(day=["Thur", "Fri", "Sat", "Sun"]))

# UI: Checkboxes to select events
st.header("Event Selectors for a Histogram chart")
with st.expander("Here is the code"):
    st.code("""
import numpy as np
import plotly.express as px

df = px.data.tips()
fig_histogram = px.histogram(df, x="day", category_orders=dict(day=["Thur", "Fri", "Sat", "Sun"]))

on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Histogram")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Histogram")
on_hover = st.checkbox("On Hover", key="oh_Histogram")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Histogram")

with st.expander("Original Data:"):
    st.write(df)

return_value = st.plotly_chart_widget(
    fig_histogram,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="histogram_chart",
)

# Optionally display return values
st.dataframe(return_value)
    """)
on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_Histogram")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_Histogram")
on_hover = st.checkbox("On Hover", key="oh_Histogram")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Histogram")

with st.expander("Original Data:"):
    st.write(df)

return_value = st.plotly_chart_widget(
    fig_histogram,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="histogram_chart",
)

# Optionally display return values
st.dataframe(return_value)


# LINE CHART
df = px.data.gapminder().query("continent=='Oceania'")
fig_linechart = px.line(df, x="year", y="lifeExp", color='country', markers=True)
# Update the configuration to enable lasso selection
fig_linechart.update_layout(dragmode='select')
# UI: Checkboxes to select events
st.header("Event Selectors for a Line Chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

# LINE CHART
df = px.data.gapminder().query("continent=='Oceania'")
fig_linechart = px.line(df, x="year", y="lifeExp", color='country', markers=True)
# Update the configuration to enable lasso selection
fig_linechart.update_layout(dragmode='select')

on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_LineChart")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_LineChart")
on_hover = st.checkbox("On Hover", key="oh_LineChart")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_LineChart")

with st.expander("Original Data:"):
    st.write(df)

return_value = st.plotly_chart_widget(
    fig_linechart,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="line_chart",
)

# Optionally display return values
st.dataframe(return_value)
    """)
on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_LineChart")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_LineChart")
on_hover = st.checkbox("On Hover", key="oh_LineChart")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_LineChart")

with st.expander("Original Data:"):
    st.write(df)

return_value = st.plotly_chart_widget(
    fig_linechart,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="line_chart",
)

# Optionally display return values
st.dataframe(return_value)

# from urllib.request import urlopen
# import json
# @st.cache_data
# def load_json(url):
#     with urlopen(url) as response:
#         counties = json.load(response)
#         return counties

# @st.cache_data  # 👈 Add the caching decorator
# def load_data(url):
#     df = pd.read_csv(url, dtype={"fips": str})
#     return df

# df = load_data("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv")
# counties = load_json("https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json")
# fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
#         color_continuous_scale="Viridis",
#         range_color=(0, 12),
#         mapbox_style="carto-positron",
#         zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
#         opacity=0.5,
#         labels={'unemp':'unemployment rate'}
#         )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# # UI: Checkboxes to select events
# st.header("Event Selectors for a Choropleth Map. Warning: This can be a little slow!")
# with st.expander("Here is the code"):
#     st.code("""
# import streamlit as st
# import plotly.express as px
# from urllib.request import urlopen
# import json

# @st.cache_data
# def load_json(url):
#     with urlopen(url) as response:
#         counties = json.load(response)
#         return counties

# @st.cache_data  # 👈 Add the caching decorator
# def load_data(url):
#     df = pd.read_csv(url, dtype={"fips": str})
#     return df

# df = load_data("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv")
# counties = load_json("https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json")
# fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
#         color_continuous_scale="Viridis",
#         range_color=(0, 12),
#         mapbox_style="carto-positron",
#         zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
#         opacity=0.5,
#         labels={'unemp':'unemployment rate'}
#         )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# on_click = st.checkbox("On Click", key="oc_Choropleth")
# on_select = st.checkbox("On Select", key="os_Choropleth")
# on_hover = st.checkbox("On Hover", key="oh_Choropleth")
# on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Choropleth")

# return_value = st.plotly_chart_widget(
#     fig,
#     theme="streamlit",
#     # Event Selector enabling is here
#     on_click=on_click,
#     on_select=on_select,
#     on_hover=on_hover,
#     on_relayout=on_relayout,
#     # END Event Selector enabling is here
#     key="Choropleth_chart",
# )

# st.dataframe(return_value)
#     """)
# on_click = st.checkbox("On Click", key="oc_Choropleth")
# on_select = st.checkbox("On Select", key="os_Choropleth")
# on_hover = st.checkbox("On Hover", key="oh_Choropleth")
# on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Choropleth")

# return_value = st.plotly_chart_widget(
#     fig,
#     theme="streamlit",
#     # Event Selector enabling is here
#     on_click=on_click,
#     on_select=on_select,
#     on_hover=on_hover,
#     on_relayout=on_relayout,
#     # END Event Selector enabling is here
#     key="Choropleth_chart",
# )

# st.dataframe(return_value)

# STACKED BAR CHART
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")

st.header("Event Selectors for a Stacked Bar Chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")

on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_StackedBar")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_StackedBar")
on_hover = st.checkbox("On Hover", key="oh_StackedBar")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_StackedBar")

with st.expander("Original Data:"):
    st.write(wide_df)

return_value = st.plotly_chart_widget(
    fig,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="StackedBar_chart",
)

st.dataframe(return_value)
    """)
on_click = st.checkbox("On Click (Select up to 1 point)", key="oc_StackedBar")
on_select = st.checkbox("On Select (Select more than 0 points through lasso or box button)", key="os_StackedBar")
on_hover = st.checkbox("On Hover", key="oh_StackedBar")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_StackedBar")

with st.expander("Original Data:"):
    st.write(wide_df)

return_value = st.plotly_chart_widget(
    fig,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="StackedBar_chart",
)

st.dataframe(return_value)
