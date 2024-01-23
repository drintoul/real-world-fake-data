import streamlit as st
from faker import Faker
import pandas as pd
import numpy as np

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')

def show_grid(columns, rows):

	for row in range(rows):
		for col in range(columns):
			st.write(row, col)

def main():
	
	col1, col2 = st.columns(2)

	with col1:
		columns = st.slider('Columns', min_value=1, max_value=10, step=1, value=1)
	with col2:
		rows = st.select_slider('Rows', options=[1, 10, 100, 1000], value=1)

	show_grid(columns, rows)

if __name__ == '__main__':
	
	main()	
