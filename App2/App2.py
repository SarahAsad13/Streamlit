import pandas as pd
import streamlit as st

st.set_page_config(page_title= 'My first streamlit file', layout='wide')
st.title("Hello, It's Toyota-Corona-1975 -A Vintage Car!") 
st.write('Yayy')

from PIL import Image
img = Image.open("toyota.jpg")
st.image(img, width=1000)

#Radio Button
status = st.radio("Select Status: ", ('Car Guy', 'Car Girl'))
if (status == 'Car Guy'):
    st.success("Car Guy")
else:
    st.success("Car Girl")

df = pd.read_csv("./cars.csv")
st.dataframe(df) 