import pandas as pd
import numpy as np
import streamlit as st

st.title('This is Shatha')
st.write('I am also known as Mugiwaraya')

data=pd.DataFrame({
    "The subject":['DENG1312','DSCI1322','DMTH1311','DPHY1211','DSCI1421'],
    "My grade":['A+','A+','A+','A+','A+']
})

st.write("My grade is")
st.write(data)

chart_data= pd.DataFrame(
    np.random.randn(20,3),
    columns=['K','A','I']
)

st.line_chart(chart_data)