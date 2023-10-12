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

import streamlit as st
import plotly.express as px

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
on_click = st.checkbox("On Click")
on_select = st.checkbox("On Select")
on_hover = st.checkbox("On Hover")
on_relayout = st.checkbox("On Relayout")

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
on_click = st.checkbox("On Click", key="oc_Bubble")
on_select = st.checkbox("On Select", key="os_Bubble")
on_hover = st.checkbox("On Hover", key="oh_Bubble")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Bubble")

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
from datetime import datetime
open_data_candlestick = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data_candlestick = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data_candlestick = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data_candlestick = [33.0, 32.9, 33.3, 33.1, 33.1]
dates_candlestick = [
    datetime(year=2013, month=10, day=10),
    datetime(year=2013, month=11, day=10),
    datetime(year=2013, month=12, day=10),
    datetime(year=2014, month=1, day=10),
    datetime(year=2014, month=2, day=10),
]
fig_candlestick = go.Figure(
    data=[
        go.Candlestick(
            x=dates_candlestick,
            open=open_data_candlestick,
            high=high_data_candlestick,
            low=low_data_candlestick,
            close=close_data_candlestick,
        )
    ]
)

# UI: Checkboxes to select events
st.header("Event Selectors for a Candlestick chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px

from datetime import datetime
open_data_candlestick = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data_candlestick = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data_candlestick = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data_candlestick = [33.0, 32.9, 33.3, 33.1, 33.1]
dates_candlestick = [
    datetime(year=2013, month=10, day=10),
    datetime(year=2013, month=11, day=10),
    datetime(year=2013, month=12, day=10),
    datetime(year=2014, month=1, day=10),
    datetime(year=2014, month=2, day=10),
]
fig_candlestick = go.Figure(
    data=[
        go.Candlestick(
            x=dates_candlestick,
            open=open_data_candlestick,
            high=high_data_candlestick,
            low=low_data_candlestick,
            close=close_data_candlestick,
        )
    ]
)

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
on_click = st.checkbox("On Click", key="oc_Candlestick")
on_select = st.checkbox("On Select", key="os_Candlestick")
on_hover = st.checkbox("On Hover", key="oh_Candlestick")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Candlestick")

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

import streamlit as st
import plotly.graph_objects as go

# BAR CHART
months = ['January', 'February', 'March', 'April', 'May']
sales = [200, 220, 250, 275, 300]
fig_bar = go.Figure(
    data=[
        go.Bar(
            x=months,
            y=sales
        )
    ]
)

# UI: Checkboxes to select events
st.header("Event Selectors for a Bar chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.graph_objects as go

# BAR CHART
months = ['January', 'February', 'March', 'April', 'May']
sales = [200, 220, 250, 275, 300]
fig_bar = go.Figure(
    data=[
        go.Bar(
            x=months,
            y=sales
        )
    ]
)

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
on_click = st.checkbox("On Click", key="oc_Bar")
on_select = st.checkbox("On Select", key="os_Bar")
on_hover = st.checkbox("On Hover", key="oh_Bar")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Bar")

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

import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Generate some data
np.random.seed(42)  # For reproducibility
x_data = np.linspace(0, 10, 100)
y_data = x_data + np.random.normal(scale=3, size=100)

# SCATTER PLOT
fig_scatter = go.Figure(data=[go.Scatter(x=x_data, y=y_data, mode='markers')])

# UI: Checkboxes to select events
st.header("Event Selectors for a Scatter Plot")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Generate some data
np.random.seed(42)  # For reproducibility
x_data = np.linspace(0, 10, 100)
y_data = x_data + np.random.normal(scale=3, size=100)

# SCATTER PLOT
fig_scatter = go.Figure(data=[go.Scatter(x=x_data, y=y_data, mode='markers')])

# UI: Checkboxes to select events
st.header("Event Selectors for a Scatter Plot")
with st.expander("Here is the code"):
    # [CODE WILL BE HERE IN THE ACTUAL APP, OMITTING HERE FOR BREVITY]

on_click = st.checkbox("On Click", key="oc_Scatter")
on_select = st.checkbox("On Select", key="os_Scatter")
on_hover = st.checkbox("On Hover", key="oh_Scatter")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Scatter")

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

on_click = st.checkbox("On Click", key="oc_Scatter")
on_select = st.checkbox("On Select", key="os_Scatter")
on_hover = st.checkbox("On Hover", key="oh_Scatter")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Scatter")

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

import numpy as np
import plotly.graph_objects as go
import streamlit as st

# HISTOGRAM CHART
data_histogram = np.random.randn(10000)  # Larger dataset

fig_histogram = go.Figure(data=[go.Histogram(x=data_histogram)])

# UI: Checkboxes to select events
st.header("Event Selectors for a Histogram chart")
with st.expander("Here is the code"):
    st.code("""
import numpy as np
import plotly.graph_objects as go
import streamlit as st

# HISTOGRAM CHART
data_histogram = np.random.randn(10000)  # Generating large dataset

fig_histogram = go.Figure(data=[go.Histogram(x=data_histogram)])

on_click = st.checkbox("On Click", key="oc_Histogram")
on_select = st.checkbox("On Select", key="os_Histogram")
on_hover = st.checkbox("On Hover", key="oh_Histogram")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Histogram")
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
on_click = st.checkbox("On Click", key="oc_Histogram")
on_select = st.checkbox("On Select", key="os_Histogram")
on_hover = st.checkbox("On Hover", key="oh_Histogram")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Histogram")

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

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# GENERATING LARGER DATASET FOR LINE CHART
np.random.seed(0)  # for reproducibility
dates_linechart = [datetime(2013, 1, 1) + timedelta(days=i) for i in range(1000)]
data_linechart = np.cumsum(np.random.randn(1000))  # Generating random walk data

fig_linechart = go.Figure(data=[go.Scatter(x=dates_linechart, y=data_linechart)])

# UI: Checkboxes to select events
st.header("Event Selectors for a Line Chart")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# LINE CHART
np.random.seed(0)
dates_linechart = [datetime(2013, 1, 1) + timedelta(days=i) for i in range(1000)]
data_linechart = np.cumsum(np.random.randn(1000))  # Generating random walk data

fig_linechart = go.Figure(data=[go.Scatter(x=dates_linechart, y=data_linechart)])

on_click = st.checkbox("On Click", key="oc_LineChart")
on_select = st.checkbox("On Select", key="os_LineChart")
on_hover = st.checkbox("On Hover", key="oh_LineChart")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_LineChart")
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
on_click = st.checkbox("On Click", key="oc_LineChart")
on_select = st.checkbox("On Select", key="os_LineChart")
on_hover = st.checkbox("On Hover", key="oh_LineChart")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_LineChart")

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
