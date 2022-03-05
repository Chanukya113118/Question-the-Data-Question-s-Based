import streamlit as st
import pandas as pd
import plotly.express as plt
def viz(data): 
    col1,col2=st.columns(2)
    viz_col=col1.multiselect('Choose Column',options=data.columns)
    viz_type=col2.selectbox('Choose graph type',['Line','Bar','Histogram','Scatter'])
    if viz_type=='Bar':
        try:
            fig=plt.bar(data,viz_col)
            st.write(fig)
        except:
            if len(viz_col) <3:
                fig=plt.bar(data[viz_col[0]],data[viz_col[1]])
                st.write(fig)
            st.write('Choose only similar data types')
    elif viz_type=='Line':
        try:
            fig=plt.line(data,viz_col)
            st.write(fig)
        except:
            if len(viz_col) <3:
                fig=plt.line(data[viz_col[0]],data[viz_col[1]])
                st.write(len(viz_col))
                st.write(fig)
            st.write('Choose only similar data types')
    elif viz_type=='Histogram':
        try:
            fig=plt.histogram(data,viz_col)
            st.write(fig)
        except:
            if len(viz_col) <3:
                fig=plt.histogram(data[viz_col[0]],data[viz_col[1]])
                st.write(len(viz_col))
    elif viz_type=='Scatter':
        try:
            fig=plt.scatter(data,viz_col)
            st.write(fig)
        except:
            if len(viz_col) <3:
                fig=plt.scatter(data[viz_col[0]],data[viz_col[1]])
                st.write(len(viz_col))
                
