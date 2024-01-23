import streamlit as st
from faker import Faker
import pandas as pd
import numpy as np

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')

def main():
	
	col1, col2 = st.columns(2)

	with col1:
		columns = st.select_slider('Columns', 1, 10, 1)
	with col2:
		rows = st.select_slider('Rows', options=[1, 10, 100, 1000])

	st.write(columns, rows)

if __name__ == '__main__':
	
	main()	
