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

st.set_page_config(
    page_title="Interactive Plotly Demo",
    page_icon="📈",
)
st.title("📈 Interactive Plotly Streamlit Demo")

st.markdown("[Download link for the streamlit wheel file](https://github.com/willhuang1997/InteractivePlotlyDemo/raw/main/streamlit-1.27.2-py2.py3-none-any.whl)")

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

def bubble_callback():
    if st.session_state.bubble_chart:
        st.dataframe(st.session_state.bubble_chart)
    else:
        st.write("There is nothing stored in st.session_state.bubble_chart")


st.header("Selections for a Bubble chart (Yes callback)")
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

def bubble_callback():
    if st.session_state.bubble_chart:
        st.dataframe(st.session_state.bubble_chart)
    else:
        st.write("There is nothing stored in st.session_state.bubble_chart")

with st.expander("Original Data:"):
    st.write(df_bubble.query("year==2007"))

st.plotly_chart(
    fig_bubble,
    on_select=bubble_callback,
    key="bubble_chart",
)

st.dataframe(st.session_state.bubble_chart)
    """)

with st.expander("Original Data:"):
    st.write(df_bubble.query("year==2007"))

st.plotly_chart(
    fig_bubble,
    on_select=bubble_callback,
    key="bubble_chart",
)

# Optionally display return values
st.dataframe(st.session_state.bubble_chart)

# BAR CHART
data_canada = px.data.gapminder().query("country == 'Canada'")
fig_bar = px.bar(data_canada, x='year', y='pop')

st.header("Selections for a Bar chart (No callback)")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

# BAR CHART
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')

st.write("Original Data:")
st.write(data_canada)

with st.expander("Original Data:"):
    st.write(data_canada)

st.plotly_chart(
    fig_bar,
    on_select=bar_callback,
    key="bar_chart",
)

# Optionally display return values
st.dataframe(st.session_state.bar_chart)
    """)

with st.expander("Original Data:"):
    st.write(data_canada)

st.plotly_chart(
    fig_bar,
    on_select=True,
    key="bar_chart",
)

# Optionally display return values
st.dataframe(st.session_state.bar_chart)

# CANDLESTICK CHART
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig_candlestick = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

st.header("Selections for a Candlestick chart")
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

with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig_candlestick,
    on_select=True,
    key="candlestick_chart",
)

# Optionally display return values
st.dataframe(st.session_state.candlestick_chart)
    """)

with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig_candlestick,
    on_select=True,
    key="candlestick_chart",
)

# Optionally display return values
st.dataframe(st.session_state.candlestick_chart)

# Generate some data
df = px.data.iris() # iris is a pandas DataFrame
fig_scatter = px.scatter(df, x="sepal_width", y="sepal_length")

st.header("Selections for a Scatter Plot")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

# Generate some data
df = px.data.iris() # iris is a pandas DataFrame
fig_scatter = px.scatter(df, x="sepal_width", y="sepal_length")


st.header("Selections for a Scatter Plot")

with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig_scatter,
    on_select=True,
    key="scatter_chart",
)

# Optionally display return values
st.dataframe(st.session_state.scatter_chart)
    """)

with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig_scatter,
    on_select=True,
    key="scatter_chart",
)

# Optionally display return values
st.dataframe(st.session_state.scatter_chart)

# HISTOGRAM CHART
df = px.data.tips()
fig_histogram = px.histogram(df, x="day", category_orders=dict(day=["Thur", "Fri", "Sat", "Sun"]))


st.header("Selections for a Histogram chart")
with st.expander("Here is the code"):
    st.code("""
import numpy as np
import plotly.express as px

df = px.data.tips()
fig_histogram = px.histogram(df, x="day", category_orders=dict(day=["Thur", "Fri", "Sat", "Sun"]))

with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig_histogram,
    on_select=True,
    key="histogram_chart",
)

# Optionally display return values
st.dataframe(return_value)
    """)

with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig_histogram,
    on_select=True,
    key="histogram_chart",
)

# Optionally display return values
st.dataframe(st.session_state.histogram_chart)


# LINE CHART
df = px.data.gapminder().query("continent=='Oceania'")
fig_linechart = px.line(df, x="year", y="lifeExp", color='country', markers=True)
# Update the configuration to enable lasso selection
fig_linechart.update_layout(dragmode='select')

st.header("Selections for a Line Chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

# LINE CHART
df = px.data.gapminder().query("continent=='Oceania'")
fig_linechart = px.line(df, x="year", y="lifeExp", color='country', markers=True)
# Update the configuration to enable lasso selection
fig_linechart.update_layout(dragmode='select')

with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig_linechart,
    on_select=True,
    key="line_chart",
)

# Optionally display return values
st.dataframe(return_value)
    """)
with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig_linechart,
    on_select=True,
    key="line_chart",
)

# Optionally display return values
st.dataframe(st.session_state.line_chart)

from urllib.request import urlopen
import json
@st.cache_data
def load_json(url):
    with urlopen(url) as response:
        counties = json.load(response)
        return counties

@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url, dtype={"fips": str})
    return df

df = load_data("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv")
counties = load_json("https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json")
fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
        color_continuous_scale="Viridis",
        range_color=(0, 12),
        mapbox_style="carto-positron",
        zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
        opacity=0.5,
        labels={'unemp':'unemployment rate'}
        )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.header("Selections on Choropleth chart")

with st.expander("Here is the code"):
    st.code("""
import streamlit as st
from urllib.request import urlopen
import json
@st.cache_data
def load_json(url):
    with urlopen(url) as response:
        counties = json.load(response)
        return counties

@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url, dtype={"fips": str})
    return df

df = load_data("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv")
counties = load_json("https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json")
fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
        color_continuous_scale="Viridis",
        range_color=(0, 12),
        mapbox_style="carto-positron",
        zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
        opacity=0.5,
        labels={'unemp':'unemployment rate'}
        )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.header("Selections on Choropleth chart")
with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig,
    on_select=True,
    key="Choropleth_chart",
)

st.dataframe(st.session_state.Choropleth_chart)
""")

with st.expander("Original Data:"):
    st.write(df)

st.plotly_chart(
    fig,
    on_select=True,
    key="Choropleth_chart",
)

st.dataframe(st.session_state.Choropleth_chart)

# STACKED BAR CHART
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")

st.header("Selections for a Stacked Bar Chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")

with st.expander("Original Data:"):
    st.write(wide_df)

st.plotly_chart(
    fig,
    on_select=True,
    key="StackedBar_chart",
)

st.dataframe(return_value)
    """)

with st.expander("Original Data:"):
    st.write(wide_df)

st.plotly_chart(
    fig,
    on_select=True,
    key="StackedBar_chart",
)

st.dataframe(st.session_state.StackedBar_chart)

data = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
fig = px.funnel(data, x='number', y='stage')
st.header("Selections for a Funnel Chart (slightly bugged as it displays half values)")
with st.expander("Original Data:"):
    st.write(data)
with st.expander("Here is the code:"):
    st.code("""
import streamlit as st
import plotly.express as px
data = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
fig = px.funnel(data, x='number', y='stage')
st.header("Selections for a Funnel Chart (slightly bugged as it displays half values)")
with st.expander("Original Data:"):
    st.write(data)
st.plotly_chart(fig, on_select=True, key="funnel_chart")
st.dataframe(st.session_state.funnel_chart)
""")
st.plotly_chart(fig, on_select=True, key="funnel_chart")
st.dataframe(st.session_state.funnel_chart)
