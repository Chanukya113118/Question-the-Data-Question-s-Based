import streamlit as st
import pandas as pd
import viz_opt 
st.title("Question the Data -- Question's Based")
file=st.file_uploader('Upload file',type=['CSV'])
try:
    if file is not None:
        data=pd.read_csv(file)
        st.title('What do you want to do with your data?')
        opt=st.radio('choose',options=['','Visualization','Analyses','Prediction'])
        if opt=='Visualization':
            viz_opt.viz(data)
        elif opt=='Analyses':
            st.write('Wait coming')
        elif opt=='Prediction':
            st.write('wait Coming')
except:
    st.write('Try only CSV files')
