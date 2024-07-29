import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
st.set_page_config(layout="wide")


df = pd.read_csv('Master_df.csv')

st.title("COUNTRIES OF THE WORLD")
col1, col2 = st.columns([1,1])
col3, col4 = st.columns([1,1])

with col1:
  

    # Quadrant 1: Scatter Plot
    st.header("Scatter Plot")
    x_axis = st.selectbox('Select X-axis', df.columns, key='scatter_x')
    y_axis = st.selectbox('Select Y-axis', df.columns, key='scatter_y')
    size = st.selectbox('Select Size', df.columns)
    countries = st.multiselect('Select Countries', df['Country'].unique())
    scatter_data = df[df['Country'].isin(countries)]
    # using fillna so that an error is not encountered
    scatter_data[size] = scatter_data[size].fillna(0)
    # setting max and min for xrange and yrange so that the points dont go out of range
    scatter_fig = px.scatter(scatter_data, x=x_axis, y=y_axis, range_x=[scatter_data[x_axis].min(), scatter_data[x_axis].max()], range_y=[scatter_data[y_axis].min(), scatter_data[y_axis].max()],size=size, color='Country', animation_frame='Year', title="Scatter Plot")
    st.plotly_chart(scatter_fig, use_container_width=True)

with col2:
    st.header("Line Chart")
    y_line_axis = st.selectbox('Select Y-axis for Line Chart', df.columns, key='line_y')
    line_countries = st.multiselect('Select Countries for Line Chart', df['Country'].unique(), key='line_countries')
    line_data = df[df['Country'].isin(line_countries)]
    line_fig = px.line(line_data, x='Year', y=y_line_axis, color='Country', title="Line Chart")
    st.plotly_chart(line_fig, use_container_width=True)

with col3:
    st.header("Bar Chart")
    y_bar_axis = st.selectbox('Select Y-axis', df.columns, key='bar_y')
    bar_countries = st.multiselect('Select Countries', df['Country'].unique(), key='bar_countries')
    bar_data = df[df['Country'].isin(bar_countries)]
    bar_fig = px.bar(bar_data, x='Country', y=y_bar_axis, color='Country', animation_frame='Year', title="Bar Chart")
    st.plotly_chart(bar_fig, use_container_width=True)


with col4:
    st.header("Pie Chart")
    pie_param = st.selectbox('Select Parameter', df.columns, key='pie')
    pie_countries = st.multiselect('Select Countries ', df['Country'].unique(), key='pie_countries')
    pie_data = df[df['Country'].isin(pie_countries)]
    pie_fig = px.pie(pie_data, names='Country', values=pie_param, title="Pie Chart")
    st.plotly_chart(pie_fig, use_container_width=True)

 