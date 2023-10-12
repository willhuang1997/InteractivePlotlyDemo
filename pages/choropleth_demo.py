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

# UI: Checkboxes to select events
st.header("Event Selectors for a Choropleth Map. Warning: This can be a little slow!")
with st.expander("Here is the code"):
    st.code("""
import streamlit as st
import plotly.express as px
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

on_click = st.checkbox("On Click", key="oc_Choropleth")
on_select = st.checkbox("On Select", key="os_Choropleth")
on_hover = st.checkbox("On Hover", key="oh_Choropleth")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Choropleth")

return_value = st.plotly_chart_widget(
    fig,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="Choropleth_chart",
)

st.dataframe(return_value)
    """)
on_click = st.checkbox("On Click", key="oc_Choropleth")
on_select = st.checkbox("On Select", key="os_Choropleth")
on_hover = st.checkbox("On Hover", key="oh_Choropleth")
on_relayout = st.checkbox("On Relayout (AKA zoom or pan)", key="or_Choropleth")

return_value = st.plotly_chart_widget(
    fig,
    theme="streamlit",
    # Event Selector enabling is here
    on_click=on_click,
    on_select=on_select,
    on_hover=on_hover,
    on_relayout=on_relayout,
    # END Event Selector enabling is here
    key="Choropleth_chart",
)

st.dataframe(return_value)
