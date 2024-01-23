import streamlit as st
from faker import Faker
import pandas as pd
import numpy as np

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')

def main():
	
	col1, col2 = st.columns(2)

	with col1:
		st.write('Columns')
		columns = st.slider('Columns', min_value=1, max_value=10, step=1, value=1)
	with col2:
		st.write('Rows')
		rows = st.select_slider('Rows', options=[1, 10, 100, 1000], value=1)

	st.write(columns, rows)

if __name__ == '__main__':
	
	main()	
