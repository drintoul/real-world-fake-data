import streamlit as st
from faker import Faker
import pandas as pd

st.set_page_config(page_title="Real World Fake Data")
st.title('Real World Fake Data')

col1, col2 = st.columns(2)
with col1:
	st.subheader('Generate Fake data in CSV')
with col2:
	st.button('Reset')

def main():

	fake = Faker()

	cols = st.slider('Enter number of columns desired', 1, 10, 1)

	coltypes = {}

	for n in range(cols):

		st.write(f'Column {n+1}')

		col1, col2 = st.columns(2)
		with col1:
			colname = st.text_input('Column name')
		with col2:
			coltype = st.selectbox('Data type', ['Birthdate', 'SSN', 'Address', 'Name'])

		coltypes[colname] = coltype

	st.write(coltypes)

	rows = st.slider('Enter number of rows desired', 1, 25, 1)

	st.write(rows)
							 
if __name__ == '__main__':
	
	main()	
